import unittest
from BankAccount import BankAccount


class BankAccountTest(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("georgi", 0, "$")
        self.account2 = BankAccount("Rado", 1000, "BGN")

    def test_create_new_bank_account(self):
        self.assertTrue(isinstance(self.account, BankAccount))

    def test_init_input(self):
        with self.assertRaises(TypeError):
            self.account = BankAccount("georgi", "", "$")

    def test_deposit_money(self):
        self.account.deposit(100)
        self.assertEqual(self.account.balance(), 100)

    def test_account_balance(self):
        self.assertEqual(self.account.balance(), 0)

    def test_withdraw_from_account(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(100)

    def test_withdraw_from_account_after_deposit(self):
        self.account.deposit(100)
        self.account.withdraw(50)
        self.assertEqual(self.account.balance(), 50)

    def test_str_dunder(self):
        test_str = 'Bank account for georgi with balance of 0$'
        self.assertEqual(str(self.account), test_str)

    def test_int_dunder(self):
        self.assertEqual(int(self.account), 0)

    def test_transfer_to(self):
        self.assertEqual(self.account2.transfer_to(self.account, 1000), True)

    def test_transfer_to_and_check_balance(self):
        self.account2.transfer_to(self.account, 1000)
        self.assertTrue(self.account.balance(), 1000)

    def test_history(self):
        self.assertEqual(self.account.history(), ['Account was created'])

if __name__ == '__main__':
    unittest.main()
