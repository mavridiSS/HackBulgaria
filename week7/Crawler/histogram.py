class Histogram:
    def __init__(self):
        self.histogram = {}

    def add(self, key):
        if key not in self.histogram:
            self.histogram[key] = 1
        else:
            self.histogram[key] += 1

    def count(self, key):
        if key in self.histogram:
            return self.histogram[key]
        else:
            return None
