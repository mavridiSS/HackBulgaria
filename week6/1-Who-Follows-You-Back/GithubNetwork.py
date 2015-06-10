import requests
import json
from settings import URL
from client_settings import CLIENT_ID, CLIENT_SECRET
from DirectedGraph import DirectedGraph


class GithubNetwork:
    FOLLOWING = 'following'
    FOLLOWERS = 'followers'

    def __init__(self, username, level):
        if level >= 4:
            raise ValueError("Dont build such a big social\
                              graph-it's going to take forever!")
        self.level = level
        self.username = username
        self.network = DirectedGraph()
        self.build_network(self.username, self.level)

    @staticmethod
    def usernames_from(source):
        return [user['login'] for user in source.json()]

    @staticmethod
    def get_network_for(user):
        network = {GithubNetwork.FOLLOWING: [], GithubNetwork.FOLLOWERS: []}
        secret = CLIENT_SECRET
        client = CLIENT_ID
        cur_followers_page = 1
        cur_following_page = 1
        has_followers = True
        has_following = True
        while has_followers:
            followers = requests.get(URL.format(user,
                                                GithubNetwork.FOLLOWERS,
                                                cur_followers_page,
                                                client, secret))
            if followers.json():
                network[GithubNetwork.FOLLOWERS] += \
                    GithubNetwork.usernames_from(followers)
            else:
                has_followers = False
            cur_followers_page += 1

        while has_following:
            following = requests.get(URL.format(user,
                                                GithubNetwork.FOLLOWING,
                                                cur_following_page,
                                                client, secret))
            if following.json():
                network[GithubNetwork.FOLLOWING] += \
                    GithubNetwork.usernames_from(following)
            else:
                has_following = False

            cur_following_page += 1

        return network

    def build_network(self, user, level):
        visited = set()
        queue = []
        visited.add(user)
        queue.append((0, user))
        while len(queue) > 0:
            curr_lvl, curr_node = queue.pop(0)
            if curr_lvl + 1 > level:
                break
            network = GithubNetwork.get_network_for(curr_node)
            for follower in network[GithubNetwork.FOLLOWERS]:
                self.network.add_edge(follower, curr_node)
                if follower not in visited:
                    visited.add(follower)
                    queue.append((curr_lvl + 1, follower))
            for following in network[GithubNetwork.FOLLOWING]:
                self.network.add_edge(curr_node, following)
                if following not in visited:
                    visited.add(following)
                    queue.append((curr_lvl + 1, following))

    def do_you_follow(self, user):
        return user in self.network.graph[self.username]

    def do_you_follow_indirectly(self, user):
        for following in self.network.graph[self.username]:
            if user in self.network.graph[following]:
                return True

        return False

    def does_he_she_follows(self, user):
        return self.username in self.network.graph[user]

    def does_he_she_follows_indirectly(self, user):
        for member in self.network.graph:
            if self.username in self.network.graph[member] \
                    and member in self.network.graph[user] \
                    and user != self.username:
                return True
        return False

    def who_follows_you_back(self):
        followers = [member for member in self.network.graph
                     if self.username in self.network.graph[member]]
        following = self.network.graph[self.username]

        first = [user for user in followers if user in following]
        second = [user for user in followers for followed in following
                  if user in self.network.graph[followed]]
        return list(set(first + second))