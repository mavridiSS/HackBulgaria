from song import Song
from tabulate import tabulate
import datetime
import json
import time
import random


class Playlist:
    def __init__(self, name, repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.playlist = []
        self.curr_song_index = 0
        self.shuffled_songs = set()

    def add_song(self, song):
        if song in self.playlist:
            raise ValueError("SongIsInPlaylist")
        self.playlist.append(song)

    def remove_song(self, song):
        self.playlist.remove(song)

    def total_length(self):
        total_len_in_sec = sum([song.length_of_song(seconds=True)
                                for song in self.playlist])

        return str(datetime.timedelta(seconds=total_len_in_sec))

    def artists(self):
        artists = [song.get_artist() for song in self.playlist]

        return {name: artists.count(name) for name in artists}

    def has_next_song(self):
        return self.curr_song_index < len(self.playlist)

    def shuffle_songs(self):
            random_song = random.choice(self.playlist)

            while random_song in self.shuffled_songs:
                random_song = random.choice(self.playlist)

            self.shuffled_songs.add(random_song)

            if len(self.playlist) == len(self.shuffled_songs):
                self.shuffled_songs = set()

            return random_song

    def next_song(self):
        if self.shuffle:
            return self.shuffle_songs()
        if not self.has_next_song() and self.repeat is False:
            raise Exception("End of playlist")
        if not self.has_next_song() and self.repeat is True:
            self.curr_song_index = 0
        song = self.playlist[self.curr_song_index]
        self.curr_song_index += 1
        return song

    def pprint_playlist(self):
        table_rows = [[song.get_artist(), song.get_song(),
                       song.length_of_song()] for song in self.playlist]
        print(tabulate(table_rows, headers=["Artist", "Song", "Length"],
              tablefmt="orgtbl"))

    def prepare_json(self):
        data = {
            "name": self.name,
            "repeat": self.repeat,
            "shuffle": self.shuffle,
            "songs": [song.__dict__ for song in self.playlist]
        }
        return data

    def save(self, indent=True):
        filename = self.name.replace(" ", "-") + ".json"

        with open(filename, "w") as f:
            f.write(json.dumps(self.prepare_json(), indent=indent))

    @staticmethod
    def load(filename):
        with open(filename, "r") as f:
            contents = f.read()
            data = json.loads(contents)
            playlist = Playlist(name=data["name"],
                                repeat=data["repeat"],
                                shuffle=data["shuffle"])
            for dict_song in data["songs"]:
                song = Song(title=dict_song["title"],
                            artist=dict_song["artist"],
                            album=dict_song["album"],
                            length=dict_song["length"])
                playlist.add_song(song)
            return playlist


def test_load():
    p = Playlist.load("Code.json")
    try:
        while True:
            song = p.next_song()
            print(str(song))
            time.sleep(1)
    except Exception as e:
        print(e)
