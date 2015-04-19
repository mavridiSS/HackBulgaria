import unittest
from panda_network import Panda
from panda_network import PandaSocialNetwork


class PandaNetworkTest(unittest.TestCase):
    def test_create_panda(self):
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        self.assertEqual(ivo.name(), "Ivo")

    def test_panda_gender(self):
        with self.assertRaises(ValueError):
            Panda("Ivo", "ivo@pandamail.com", "mal")

    def test_panda_name(self):
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        self.assertEqual(ivo.name(), "Ivo")

    def test_panda_email(self):
        with self.assertRaise(ValueError):
            Panda("Ivo", "ivopandamail.com", "mal")

    def test_panda_str(self):
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        ivo_in_str = "Ivo is male panda with email: ivo@pandamail.com"
        self.assertEqual(str(ivo), ivo_in_str)

    def test_add_existing_panda_in_network(self):
        panda_netw = PandaSocialNetwork()
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        panda_netw.add_panda(ivo)
        with self.assertRaises(Exception):
            panda_netw.add_panda(ivo)

    def test_add_new_panda_in_network(self):
        panda_netw = PandaSocialNetwork()
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        panda_netw.add_panda(ivo)
        self.assertEqual(panda_netw.network[ivo], [])

    def test_has_panda_in_network(self):
        panda_netw = PandaSocialNetwork()
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        self.assertFalse(panda_netw.has_panda(ivo))

    def test_make_excisting_friends(self):
        panda_netw = PandaSocialNetwork()
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        rado = Panda("Rado", "rado@pandamail.com", "male")
        panda_netw.make_friends(ivo, rado)
        with self.assertRaises(Exception):
            panda_netw.make_friends(ivo, rado)

    def test_make_new_friends(self):
        panda_netw = PandaSocialNetwork()
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        rado = Panda("Rado", "rado@pandamail.com", "male")
        self.assertEqual(panda_netw.make_friends(ivo, rado), None)

    def test_are_friends(self):
        panda_netw = PandaSocialNetwork()
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        rado = Panda("Rado", "rado@pandamail.com", "male")
        panda_netw.make_friends(ivo, rado)
        self.assertTrue(panda_netw.are_friends(ivo, rado))

    def test_friends_of_panda_with_no_friends(self):
        panda_netw = PandaSocialNetwork()
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        self.assertFalse(panda_netw.friends_of(ivo))

    def test_friends_of_panda_with_friends(self):
        panda_netw = PandaSocialNetwork()
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        rado = Panda("Rado", "rado@pandamail.com", "male")
        panda_netw.make_friends(ivo, rado)
        self.assertEqual(panda_netw.friends_of(ivo), panda_netw.network[ivo])

    def test_connection_level_between_friends(self):
        panda_netw = PandaSocialNetwork()
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        rado = Panda("Rado", "rado@pandamail.com", "male")
        panda_netw.make_friends(ivo, rado)
        self.assertEqual(panda_netw.connection_level(ivo, rado), 1)

    def test_connection_level_with_not_existing_panda(self):
        panda_netw = PandaSocialNetwork()
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        rado = Panda("Rado", "rado@pandamail.com", "male")
        self.assertFalse(panda_netw.connection_level(ivo, rado), False)

    def test_no_connection_level(self):
        panda_netw = PandaSocialNetwork()
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        rado = Panda("Rado", "rado@pandamail.com", "male")
        gosho = Panda("Gosho", "gosho@pandamail.com", "female")
        panda_netw.add_panda(ivo)
        panda_netw.add_panda(gosho)
        panda_netw.add_panda(rado)
        panda_netw.make_friends(ivo, rado)
        self.assertFalse(panda_netw.connection_level(ivo, gosho), False)

    def test_connection_level(self):
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        rado = Panda("Rado", "rado@pandamail.com", "female")
        gosho = Panda("Gosho", "gosho@pandamail.com", "male")
        petko = Panda("Petko", "gosho@pandamail.com", "male")
        sashko = Panda("Sasho", "gosho@pandamail.com", "male")
        rashko = Panda("Rashko", "gosho@pandamail.com", "male")
        a = PandaSocialNetwork()
        a.add_panda(ivo)
        a.add_panda(rado)
        a.add_panda(gosho)
        a.make_friends(ivo, rado)
        a.make_friends(ivo, gosho)
        a.make_friends(rado, petko)
        a.make_friends(petko, gosho)
        a.make_friends(gosho, sashko)
        a.make_friends(petko, rashko)
        self.assertEqual(a.connection_level(ivo, rashko), 3)

    def test_how_many_gender(self):
        panda_netw = PandaSocialNetwork()
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        rado = Panda("Rado", "rado@pandamail.com", "male")
        panda_netw.make_friends(ivo, rado)
        self.assertEqual(panda_netw.how_many_gender_in_network(1, ivo,
                                                               "male"), 1)

if __name__ == '__main__':
    unittest.main()
