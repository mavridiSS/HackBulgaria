# Duck Typing
class Panda:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.weight = 30

    def eat(self, amount):
        self.weight += amount // 2

# Mutirasht metod
    def grow_up(self):
        self.age += 1

    def sleep(self):
        self.weight += 1

    def __add__(self, other):
        return Panda("".join([self.name, other.name]))

    def __str__(self):
        return "I am panda {} and I am {} old".format(self.name, self.age)

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.name + str(self.weight))

    def __eq__(self, other):
        return self.weight == other.weight and self.name == other.name

    def __int__(self):
        return self.weight

ivo = Panda("Ivo")
print(str(ivo))
print(int(ivo))
print(repr(ivo))