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

    def connection_level(self, panda1, panda2):
        visited = list()
        queue = list()
        counter = 0
        if self.has_panda(panda1) == False or self.has_panda(panda2) == False:
            return False
        if panda2 in self.friends_of(panda1):
            return 1
        queue.append(panda1)
        visited.append(panda1)
        while len(queue) > 0:
            t = queue.pop(0)
            if t == panda2:
                return counter
            else:
                counter += 1
                for panda in self.friends_of(t):
                    for item in self.friends_of(panda):
                        if item == panda2:
                            return counter + 1
                    if panda not in visited:
                        queue.append(panda)
                        visited.append(panda)
        return False

    def are_connected(self, panda1, panda2):
        if type(self.connection_level(panda1, panda2)) == int:
            return True
        return False

    def how_many_gender_in_network(self, level, panda, gender):
        

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
                for friends in json_network[panda]:
                    panda2 = Panda(friends["_name"],
                                   friends["_email"],
                                   friends["_gender"])
                    panda1 = eval(panda)
                    if not network.has_panda(panda2):
                        network.add_panda(panda2)
                    if not network.are_friends(panda1, panda2):
                        network.make_friends(panda1, panda2)
        return network


ivo = Panda("Ivo", "ivo@pandamail.com", "male")
rado = Panda("Rado", "rado@pandamail.com", "female")
gosho = Panda("Gosho", "gosho@pandamail.com", "male")
petko = Panda("Petko", "gosho@pandamail.com", "male")
sashko = Panda("Sasho", "gosho@pandamail.com", "male")
rashko = Panda("Rashko", "gosho@pandamail.com", "male")
a = PandaSocialNetwork()
a.make_friends(ivo, rado)
a.make_friends(ivo, gosho)
a.make_friends(rado, petko)
a.save("test.txt")
print(PandaSocialNetwork2.load("test.txt"))
