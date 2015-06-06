import unittest
from song import Song


class TestSongClass(unittest.TestCase):
    def setUp(self):
        self.song = Song(title="Odin", artist="Manowar",
                         album="The Sons of Odin", length="1:3:44")

    def test_init(self):
        self.assertTrue(isinstance(self.song, Song))

    def test_str_dunder(self):
        str_to_match = "Manowar - Odin from The Sons of Odin - 1:3:44"
        self.assertEqual(str(self.song), str_to_match)

    def test_eq_dunder(self):
        eq_song = Song(title="Odin", artist="Manowar",
                       album="The Sons of Odin", length="1:3:44")
        self.assertTrue(self.song == eq_song)

    def test_to_seconds(self):
        self.assertEqual(self.song.to_seconds(self.song.length), 3824)

    def test_length_of_song_in_seconds(self):
        self.assertEqual(self.song.length_of_song(seconds=True), 3824)

    def test_length_of_song_in_minutes(self):
        self.assertEqual(self.song.length_of_song(minutes=True), 63)

    def test_length_of_song_in_hours(self):
        self.assertEqual(self.song.length_of_song(hours=True), 1)

if __name__ == '__main__':
    unittest.main()
