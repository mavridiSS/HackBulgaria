class Song:
    def __init__(self, title, artist, album, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length

    def __str__(self):
        return "{} - {} from {} - {}".format(self.artist, self.title,
                                             self.album, self.length)

    def __hash__(self):
        return hash(self.__str__())

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def get_artist(self):
        return self.artist

    def get_song(self):
        return self.title

    def to_seconds(self, time):
        seconds = 0
        for part in time.split(":"):
            seconds = seconds * 60 + int(part)
        return seconds

    def length_of_song(self, seconds=False, minutes=False, hours=False):
        if seconds:
            return self.to_seconds(self.length)
        if minutes:
            return self.to_seconds(self.length) // 60
        if hours:
            return self.to_seconds(self.length) // 3600
        else:
            return self.length


