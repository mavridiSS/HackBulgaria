import sys
import unittest
import os
import uuid

sys.path.append("..")
import sql_manager


class SqlManagerTests(unittest.TestCase):

    def setUp(self):
        sql_manager.create_clients_table()
        sql_manager.register('Tester', 'Test12345', 'tester@abv.bg')

    def tearDown(self):
        sql_manager.cursor.execute('DROP TABLE clients')

    @classmethod
    def tearDownClass(cls):
        os.remove("bank.db")

    def test_if_strong_password(self):
        result = sql_manager.check_if_strong_password('Ivo', 'Ivan23456')
        self.assertTrue(result)

    def test_hash(self):
        result = sql_manager.get_hash("i")
        h_str = '042dc4512fa3d391c5170cf3aa61e6a638f84342'
        self.assertEqual(result, h_str)

    def test_register(self):
        sql_manager.register('Dinko', 'Test12345', 'dinko@abv.bg')
        hashpass = sql_manager.get_hash('Test12345')
        sql_manager.cursor.execute('SELECT Count(*)  FROM clients WHERE username =? AND password =? AND email=?', ('Dinko', hashpass, 'dinko@abv.bg'))
        users_count = sql_manager.cursor.fetchone()

        self.assertEqual(users_count[0], 1)

    def test_login(self):
        logged_user = sql_manager.login('Tester', 'Test12345')
        self.assertEqual(logged_user.get_username(), 'Tester')

    def test_login_wrong_password(self):
        logged_user = sql_manager.login('Ivan', '1')
        self.assertFalse(logged_user)

    def test_change_message(self):
        logged_user = sql_manager.login('Tester', 'Test12345')
        new_message = "podaivinototam"
        sql_manager.change_message(new_message, logged_user)
        self.assertEqual(logged_user.get_message(), new_message)

    def test_change_password(self):
        logged_user = sql_manager.login('Tester', 'Test12345')
        new_password = "12345"
        query = sql_manager.change_pass(new_password, logged_user)
        self.assertFalse(query)

    def test_balance(self):
        logged_user = sql_manager.login('Tester', 'Test12345')
        blnc = sql_manager.balance(logged_user.get_username())
        self.assertEqual(blnc, 0.0)

    def test_update_balance(self):
        logged_user = sql_manager.login('Tester', 'Test12345')
        sql_manager.update_balance(100, logged_user.get_username())
        blnc = sql_manager.balance(logged_user.get_username())
        self.assertEqual(blnc, 100)

    def test_deposit(self):
        logged_user = sql_manager.login('Tester', 'Test12345')
        sql_manager.deposit(100, logged_user.get_username())
        blnc = sql_manager.balance(logged_user.get_username())
        self.assertEqual(blnc, 100)

    def test_withdraw(self):
        logged_user = sql_manager.login('Tester', 'Test12345')
        sql_manager.deposit(100, logged_user.get_username())
        sql_manager.withdraw(50, logged_user.get_username())
        blnc = sql_manager.balance(logged_user.get_username())
        self.assertEqual(blnc, 50)

    def test_withdraw_more_than_crr_balance(self):
        logged_user = sql_manager.login('Tester', 'Test12345')
        sql_manager.deposit(100, logged_user.get_username())
        self.assertFalse(sql_manager.withdraw(150, logged_user.get_username()))

    def test_update_code_to_reset(self):
        code = uuid.uuid4().hex
        sql_manager.update_code_to_reset(code, 1)
        select_query = 'SELECT code_to_reset FROM clients WHERE id=?'
        sql_manager.cursor.execute(select_query, (1, ))
        code_to_reset = sql_manager.cursor.fetchone()
        self.assertEqual(code, code_to_reset[0])

    def test_tan_code(self):
        code = uuid.uuid4().hex[0:32]
        sql_manager.update_tan_code(code, 1)
        select_query = 'SELECT tan_code FROM clients WHERE id=?'
        sql_manager.cursor.execute(select_query, (1, ))
        tan_code = sql_manager.cursor.fetchone()
        self.assertEqual(code, tan_code[0])

    def test_check_tan_code(self):
        logged_user = sql_manager.login('Tester', 'Test12345')
        username = logged_user.get_username()
        code = uuid.uuid4().hex[0:32]
        sql_manager.update_tan_code(code, 1)
        result = sql_manager.check_tan_code('asd', username)
        self.assertFalse(result)

    def test_check_code_to_reset(self):
        code = uuid.uuid4().hex
        sql_manager.update_code_to_reset(code, 1)
        self.assertFalse(sql_manager.check_code_to_reset('a', 'Tester'))


if __name__ == '__main__':
    unittest.main()
