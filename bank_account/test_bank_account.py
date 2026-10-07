import unittest

from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("Иван Иванов", "123456")
        self.other_account = BankAccount("Петр Петров", "654321")

    def test_account_creation(self):
        self.assertEqual(self.account.owner, "Иван Иванов")
        self.assertEqual(self.account.account_number, "123456")
        self.assertEqual(self.account.get_balance(), 0)

    def test_deposit(self):
        self.account.deposit(1000)
        self.assertEqual(self.account.get_balance(), 1000)

    def test_multiple_deposits(self):
        self.account.deposit(1000)
        self.account.deposit(500)
        self.assertEqual(self.account.get_balance(), 1500)

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    def test_deposit_zero(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0)

    def test_deposit_invalid_type(self):
        with self.assertRaises(TypeError):
            self.account.deposit("100")

    def test_withdraw(self):
        self.account.deposit(1000)
        self.account.withdraw(400)
        self.assertEqual(self.account.get_balance(), 600)

    def test_withdraw_all_money(self):
        self.account.deposit(1000)
        self.account.withdraw(1000)
        self.assertEqual(self.account.get_balance(), 0)

    def test_withdraw_more_than_balance(self):
        self.account.deposit(500)

        with self.assertRaises(ValueError):
            self.account.withdraw(600)

        self.assertEqual(self.account.get_balance(), 500)

    def test_withdraw_negative_amount(self):
        self.account.deposit(500)

        with self.assertRaises(ValueError):
            self.account.withdraw(-100)

        self.assertEqual(self.account.get_balance(), 500)

    def test_withdraw_invalid_type(self):
        with self.assertRaises(TypeError):
            self.account.withdraw("100")

    def test_transfer(self):
        self.account.deposit(1000)

        self.account.transfer(self.other_account, 400)

        self.assertEqual(self.account.get_balance(), 600)
        self.assertEqual(self.other_account.get_balance(), 400)

    def test_transfer_equal_amount(self):
        self.account.deposit(1000)

        self.account.transfer(self.other_account, 300)

        self.assertEqual(1000 - self.account.get_balance(), 300)
        self.assertEqual(self.other_account.get_balance(), 300)

    def test_transfer_more_than_balance(self):
        self.account.deposit(500)

        with self.assertRaises(ValueError):
            self.account.transfer(self.other_account, 600)

        self.assertEqual(self.account.get_balance(), 500)
        self.assertEqual(self.other_account.get_balance(), 0)

    def test_transfer_negative_amount(self):
        self.account.deposit(500)

        with self.assertRaises(ValueError):
            self.account.transfer(self.other_account, -100)

        self.assertEqual(self.account.get_balance(), 500)
        self.assertEqual(self.other_account.get_balance(), 0)

    def test_transfer_invalid_type(self):
        self.account.deposit(500)

        with self.assertRaises(TypeError):
            self.account.transfer(self.other_account, "100")

    def test_get_balance(self):
        self.account.deposit(1000)
        self.account.withdraw(250)
        self.assertEqual(self.account.get_balance(), 750)

    def test_empty_account(self):
        self.assertTrue(self.account.is_empty())

    def test_not_empty_account(self):
        self.account.deposit(100)
        self.assertFalse(self.account.is_empty())

    def test_empty_after_withdraw(self):
        self.account.deposit(500)
        self.account.withdraw(500)
        self.assertTrue(self.account.is_empty())


if __name__ == "__main__":
    unittest.main()