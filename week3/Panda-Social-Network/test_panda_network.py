import unittest
from panda_network import Panda
from panda_network import PandaSocialNetwork


class PandaNetworkTest(unittest.TestCase):
    def setUp(self):
        self.test_netw = PandaSocialNetwork()
        self.panda1 = Panda("Ivo", "ivo@pandamail.com", "male")
        self.panda2 = Panda("Rado", "rado@pandamail.com", "male")
        self.panda3 = Panda("Gosho", "gosho@pandamail.com", "male")
        self.panda4 = Panda("Petko", "gosho@pandamail.com", "male")
        self.panda5 = Panda("Sasho", "gosho@pandamail.com", "male")
        self.panda6 = Panda("Rashko", "gosho@pandamail.com", "male")

    def test_create_panda(self):
        self.assertEqual(self.panda1.name(), "Ivo")

    def test_panda_gender(self):
        with self.assertRaises(ValueError):
            Panda("Ivo", "ivo@pandamail.com", "mal")

    def test_panda_name(self):
        self.assertEqual(self.panda1.name(), "Ivo")

    def test_panda_email(self):
        with self.assertRaises(ValueError):
            Panda("Ivo", "ivopandamail.com", "mal")

    def test_panda_str(self):
        test_str = "Ivo is male panda with email: ivo@pandamail.com"
        self.assertEqual(str(self.panda1), test_str)

    def test_add_existing_panda_in_network(self):
        self.test_netw.add_panda(self.panda1)
        with self.assertRaises(Exception):
            self.test_netw.add_panda(self.panda1)

    def test_add_new_panda_in_network(self):
        self.test_netw.add_panda(self.panda1)
        self.assertEqual(self.test_netw.network[self.panda1], [])

    def test_has_panda_in_network(self):
        self.assertFalse(self.test_netw.has_panda(self.panda1))

    def test_make_excisting_friends(self):
        self.test_netw.make_friends(self.panda1, self.panda2)
        with self.assertRaises(Exception):
            self.test_netw.make_friends(self.panda1, self.panda2)

    def test_make_new_friends(self):
        self.test_netw.make_friends(self.panda1, self.panda2)
        self.assertTrue(self.panda2 in self.test_netw.network[self.panda1] and
                        self.panda1 in self.test_netw.network[self.panda2])

    def test_are_friends(self):
        self.test_netw.make_friends(self.panda1, self.panda2)
        self.assertTrue(self.test_netw.are_friends(self.panda1, self.panda2))

    def test_friends_of_panda_with_no_friends(self):
        self.assertFalse(self.test_netw.friends_of(self.panda1))

    def test_friends_of_panda_with_friends(self):
        self.test_netw.make_friends(self.panda1, self.panda2)
        self.assertEqual(self.test_netw.friends_of(self.panda1),
                         self.test_netw.network[self.panda1])

    def test_connection_level_between_friends(self):
        self.test_netw.make_friends(self.panda1, self.panda2)
        level = self.test_netw.connection_level(self.panda1, self.panda2)
        self.assertEqual(level, 1)

    def test_non_friend_pandas_connection_level(self):
        level = self.test_netw.connection_level(self.panda1, self.panda2)
        self.assertFalse(level)

    def test_connection_level(self):
        self.test_netw.add_panda(self.panda1)
        self.test_netw.add_panda(self.panda2)
        self.test_netw.add_panda(self.panda3)
        self.test_netw.add_panda(self.panda4)
        self.test_netw.add_panda(self.panda5)
        self.test_netw.add_panda(self.panda6)
        self.test_netw.make_friends(self.panda1, self.panda2)
        self.test_netw.make_friends(self.panda1, self.panda3)
        self.test_netw.make_friends(self.panda2, self.panda4)
        self.test_netw.make_friends(self.panda4, self.panda3)
        self.test_netw.make_friends(self.panda3, self.panda5)
        self.test_netw.make_friends(self.panda4, self.panda6)
        level = self.test_netw.connection_level(self.panda1, self.panda6)
        self.assertEqual(level, 3)

    def test_how_many_gender(self):
        self.test_netw.make_friends(self.panda1, self.panda2)
        result = self.test_netw.how_many_gender_in_network(1,
                                                           self.panda1,
                                                           "male")
        self.assertEqual(result, 1)

    def test_save(self):
        self.test_netw.add_panda(self.panda1)
        self.test_netw.save("test.txt")
        with open("test.txt", "r") as f:
            contents = f.read()

        self.assertEqual(self.test_netw.__repr__(), contents)

    def test_load(self):
        pass


if __name__ == '__main__':
    unittest.main()
