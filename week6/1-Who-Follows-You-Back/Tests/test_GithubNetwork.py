import unittest
from GithubNetwork import GithubNetwork


class TestGithubNetwork(unittest.TestCase):
    def setUp(self):
        self.netw = GithubNetwork('mavridiSS', 2)

    def test_get_network_for(self):
        pass

    def test_do_you_follow(self):
        user = 'RadoRado'
        self.assertTrue(self.netw.do_you_follow(user))

    def test_who_follows_you_back(self):
        followers = ['stoilyanchev']
        self.assertEqual(self.netw.who_follows_you_back(), followers)

    def test_do_you_follow_indirectly(self):
        user = 'miglen'
        self.assertFalse(self.netw.do_you_follow_indirectly(user))

    def test_does_he_she_follows(self):
        self.assertTrue(self.netw.does_he_she_follows('stoilyanchev'))

    def test_does_he_she_follows_indirectly(self):
        self.assertTrue(self.netw.does_he_she_follows_indirectly('miglen'))

if __name__ == '__main__':
    unittest.main()