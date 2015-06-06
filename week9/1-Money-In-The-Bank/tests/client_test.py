import sys
import unittest
sys.path.append("..")

from Client import Client


class ClientTests(unittest.TestCase):

    def setUp(self):
        self.test_client = Client(1, "Ivo", 'ivo@abv.bg', 20.00, "Bitcoin")

    def test_client_id(self):
        self.assertEqual(self.test_client.get_id(), 1)

    def test_client_name(self):
        self.assertEqual(self.test_client.get_username(), "Ivo")

    def test_client_balance(self):
        self.assertEqual(self.test_client.get_balance(), 20.00)

    def test_client_message(self):
        msg = self.test_client.get_message()
        self.assertEqual(msg, "Bitcoin")

    def test_client_email(self):
        mail = self.test_client.get_email()
        self.assertEqual(mail, 'ivo@abv.bg')


if __name__ == '__main__':
    unittest.main()
