import unittest
from playlist import Playlist
from song import Song


class TestPlaylistClass(unittest.TestCase):
    def setUp(self):
        self.code_songs = Playlist(name="Code")
        self.song = Song(title="Odin", artist="Manowar",
                         album="The Sons of Odin", length="1:3:44")

    def test_init(self):
        self.assertTrue(isinstance(self.code_songs, Playlist))

    def test_add_song(self):
        self.code_songs.add_song(self.song)
        with self.assertRaises(ValueError):

            self.code_songs.add_song(self.song)

    def test_remove_song(self):
        self.code_songs.add_song(self.song)
        self.code_songs.remove_song(self.song)
        self.assertEqual(self.code_songs.playlist, [])

    def test_remove_song_that_not_exist(self):
        with self.assertRaises(ValueError):
            self.code_songs.remove_song(self.song)

    def test_total_length(self):
        self.second_song = Song("I'm not afraid", "Eminem",
                                "The rehab", length="1:3:44")
        self.code_songs.add_song(self.song)
        self.code_songs.add_song(self.second_song)
        self.assertEqual(self.code_songs.total_length(), "2:07:28")

    def test_artist(self):
        self.code_songs.add_song(self.song)
        self.assertEqual(self.code_songs.artists(), {'Manowar': 1})

    def test_has_next_song(self):
        self.code_songs.add_song(self.song)
        self.assertTrue(self.code_songs.has_next_song())

    def test_save(self):
        self.s = Song(album="The Sons of Odin", title="Odin",
                      artist="Manowar", length="3:44")
        self.s1 = Song(album="The Sonds of Odin", title="Sons of Odin",
                       artist="Manowar", length="6:08")
        self.code_songs.add_song(self.s)
        self.code_songs.add_song(self.s1)
        self.code_songs.add_song(self.song)
        self.code_songs.save()
        self.assertIsNone(self.code_songs.save())

    def test_load(self):
        self.s = Song(album="The Sons of Odin", title="Odin",
                      artist="Manowar", length="3:44")
        self.s1 = Song(album="The Sonds of Odin", title="Sons of Odin",
                       artist="Manowar", length="6:08")
        self.code_songs.add_song(self.s)
        self.code_songs.add_song(self.s1)
        self.code_songs.add_song(self.song)
        self.code_songs.save()
        p = Playlist.load("Code.json")
        self.assertEqual(self.code_songs.__dict__, p.__dict__)

if __name__ == '__main__':
    unittest.main()
