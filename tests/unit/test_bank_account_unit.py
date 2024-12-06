import unittest
from BankAccount import BankAccount

class TestBankAccountUnit(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount()

    def test_deposit_valid(self):
        self.assertEqual(self.account.deposit(100), 100)
    
    def test_deposit_invalid(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-50)
    
    def test_withdraw_valid(self):
        self.account.deposit(100)
        self.assertEqual(self.account.withdraw(50), 50)
    
    def test_withdraw_invalid(self):
        self.account.deposit(100)
        with self.assertRaises(ValueError):
            self.account.withdraw(150)

    def test_balance(self):
        self.account.deposit(200)
        self.account.withdraw(50)
        self.assertEqual(self.account.get_balance(), 150)

if __name__ == "__main__":
    unittest.main()
