from song import Song
from playlist import Playlist
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
import datetime
import os


class MusicCrawler:
    def __init__(self, path):
        self.path = path

    def getTags(self, path):
        m = MP3(self.path + path, ID3=EasyID3)
        if 'title' in m and 'artist' in m and 'album' in m:
            song = Song(m['title'][0], m['artist'][0], m['album'][0],
                        datetime.timedelta(seconds=m.info.length))
            return song
        else:
            raise Exception(path + " has unknown tags and"
                                 + " can't be added to playlist.")

    def generate_playlist(self, name):
        p = Playlist(name=name)
        mp3_files = [f for f in os.listdir(self.path) if f.endswith('.mp3')]
        for file in mp3_files:
            try:
                p.add_song(self.getTags(file))
            except Exception as e:
                print(e)
        return p.pprint_playlist()


a = MusicCrawler("/home/georgi/Desktop/music/")
a.generate_playlist("MyPlaylist")
