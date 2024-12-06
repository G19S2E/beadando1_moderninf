import unittest
from BankAccount import BankAccount

class TestBankAccountIntegration(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount()

    def test_deposit_withdraw_integration(self):
        self.account.deposit(200)
        self.assertEqual(self.account.get_balance(), 200)
        
        self.account.withdraw(100)
        self.assertEqual(self.account.get_balance(), 100)

if __name__ == "__main__":
    unittest.main()
