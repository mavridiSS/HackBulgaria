import unittest
from settings import DB_NAME, DB_SQL_FILE
from last_hr import HackBulgariaDB


class TestLastHR(unittest.TestCase):
    def setUp(self):
        self.db = HackBulgariaDB()

#need to test database creation and if it is empty or not after populating the table
    def test_populate_tables(self):
        self.assertNone(self.db.populate_tables())

if __name__ == '__main__':
    unittest.main()
