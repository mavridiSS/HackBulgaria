import unittest
from BankAccount import BankAccount


class BankAccountTest(unittest.TestCase):
    def test_create_new_bank_account(self):
        account = BankAccount("georgi", 0, "$")
        self.assertTrue(isinstance(account, BankAccount))

    def test_init_input(self):
        with self.assertRaises(TypeError):
            account = BankAccount("georgi", "", "$")

    def test_deposit_money(self):
        account = BankAccount("georgi", 0, "$")
        self.assertIsNone(account.deposit(10))

    def test_deposit_money2(self):
        account = BankAccount("georgi", 0, "$")
        account.deposit(100)
        self.assertEqual(account.balance(), 100)

    def test_account_balance(self):
        account = BankAccount("georgi", 0, "$")
        self.assertEqual(account.balance(), 0)

    def test_withdraw_from_account(self):
        account = BankAccount("georgi", 50, "$")
        with self.assertRaises(ValueError):
            account.withdraw(100)

    def test_withdraw_from_account_after_deposit(self):
        account = BankAccount("georgi", 0, "$")
        account.deposit(100)
        account.withdraw(50)
        self.assertEqual(account.balance(), 50)

    def test_str_dunder(self):
        account = BankAccount("georgi", 0, "$")
        self.assertEqual(str(account), 'Bank account for georgi' +
                                        ' with balance of 0$')

    def test_int_dunder(self):
        account = BankAccount("georgi", 0, "$")
        self.assertEqual(int(account), 0)

    def test_transfer_to(self):
        rado = BankAccount("Rado", 1000, "BGN")
        ivo = BankAccount("Ivo", 0, "BGN")
        self.assertEqual(rado.transfer_to(ivo, 1000), True)

    def test_transfer_to_and_check_balance(self):
        rado = BankAccount("Rado", 1000, "BGN")
        ivo = BankAccount("Ivo", 0, "BGN")
        rado.transfer_to(ivo, 1000)
        self.assertTrue(ivo.balance(), 1000)

    def test_history(self):
        ivo = BankAccount("Ivo", 0, "BGN")
        ivo.balance()
        self.assertEqual(ivo.history(), ['Account was created',
                                         'Balance check -> 0BGN'])

if __name__ == '__main__':
    unittest.main()
