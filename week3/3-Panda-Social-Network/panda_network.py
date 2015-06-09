import json
import re


def from_dictionary_values(dictionary):
    result = []
    for key, value in dictionary.items():
        if key == '_name':
            result.insert(0, value)
        elif key == '_email':
            result.insert(1, value)
        elif key == '_gender':
            result.insert(2, value)
    return result


class Panda:

    def __init__(self, name, email, gender):
        if not re.match(r'\w[\w\.-]*@\w[\w\.-]+\.\w+', email):
            raise ValueError
        if not (gender == 'male' or gender == 'female'):
            raise ValueError
        self._email = email
        self._name = name
        self._gender = gender

    def name(self):
        return self._name

    def email(self):
        return self._email

    def gender(self):
        return self._gender

    def isMale(self):
        return self._gender == 'male'

    def isFemale(self):
        return self._gender == 'female'

    def __str__(self):
        return "{} is {} panda with email: {}".format(self._name, self._gender,
                                                      self._email)

    def __repr__(self):
        return "Panda('{}', '{}', '{}')".format(self.name(),
                                                self.email(), self.gender())

    def __eq__(self, other):
        return (self._name == other._name and
                self._gender == other._gender and
                self._email == other._email)

    def __hash__(self):
        return hash(self._name + self._email)

    def prepare_json(self):
        panda_dict = self.__dict__
        return {key: panda_dict[key] for key in panda_dict}


class PandaSocialNetwork:
    def __init__(self):
        self.network = {}

    def add_panda(self, panda):
        if panda in self.network.keys():
            raise Exception("PandaAlreadyExist")
        self.network[panda] = []

    def has_panda(self, panda):
        return panda in self.network

    def make_friends(self, panda1, panda2):
        if self.has_panda(panda1) == False:
            self.add_panda(panda1)

        if self.has_panda(panda2) == False:
            self.add_panda(panda2)

        if self.are_friends(panda1, panda2):
            raise Exception("PandasAlreadyFriends")

        self.network[panda1].append(panda2)
        self.network[panda2].append(panda1)

    def are_friends(self, panda1, panda2):
        return panda1 in self.network[panda2] and\
               panda2 in self.network[panda1]

    def friends_of(self, panda):
        if self.has_panda(panda):
            return self.network[panda]
        return False

    def network_of_connections(self, panda):
        network = {}
        visited = set()
        q = []

        q.append((0, panda))
        visited.add(panda)

        while len(q) > 0:
            level, node = q.pop(0)
            network[node] = level
            if self.friends_of(node):
                for panda in self.friends_of(node):
                    if panda not in visited:
                        q.append((level + 1, panda))
                        visited.add(panda)
        return network

    def connection_level(self, panda1, panda2):
        network = self.network_of_connections(panda1)

        if panda2 in network:
            return network[panda2]
        else:
            return False

    def are_connected(self, panda1, panda2):
        if type(self.connection_level(panda1, panda2)) == int:
            return True
        return False

    def how_many_gender_in_network(self, level, panda, gender):
        network = self.network_of_connections(panda)
        counter = 0
        for panda in network:
            if (panda.gender() == gender
                and network[panda] <= level
                    and network[panda] != 0):
                counter += 1
        return counter

    def __repr__(self):
        for_save = {}

        for panda in self.network:
            friends = [panda_friend.__dict__ for panda_friend
                       in self.network[panda]]
            for_save[repr(panda)] = friends

        return json.dumps(for_save, indent=True)

    def save(self, file_name):
        with open(file_name, 'w') as outfile:
            outfile.write(self.__repr__())

    @staticmethod
    def load(file_name):
        network = PandaSocialNetwork()
        with open(file_name, "r") as f:
            contents = f.read()
            json_network = json.loads(contents)
            for panda in json_network:
                panda1 = eval(panda)
                if not network.has_panda(panda1):
                    network.add_panda(panda1)
                for friend in json_network[panda]:
                    panda2 = Panda(friend["_name"],
                                   friend["_email"],
                                   friend["_gender"])
                    if not network.has_panda(panda2):
                        network.add_panda(panda2)
                    if not network.are_friends(panda1, panda2):
                        network.make_friends(panda1, panda2)
        return network
