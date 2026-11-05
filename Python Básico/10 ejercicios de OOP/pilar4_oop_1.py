"""Representing a banking system"""
class  BankAccount:
    """Represents a bank account that lets you deposit and withdraw money"""
    def __init__(self, owner, balance):
        """Initialize the account with the owner and the initial balance."""
        if balance < 0:
            raise ValueError("Negative balances are not allowed")
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Deposit money into the account"""
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero")
        self.balance = self.balance + amount

    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount <= 0 or amount > self.balance:
            raise ValueError("Transaction not allowed")
        self.balance = self.balance - amount


class SavingsAccount(BankAccount):
    """It represents a savings account with a mandatory minimum balance"""
    def __init__(self, owner, balance, min_balance):
        """Initialize the savings account with its minimum balance"""
        super().__init__(owner, balance)
        self.min_balance = min_balance


    def withdraw(self, amount):
        """Withdraw money without letting the balance go below the minimum"""
        if self.balance - amount < self.min_balance:
            raise ValueError("Transaction not allowed")
        super().withdraw(amount)

savings_account_1 = SavingsAccount("Steven", 1000, 100)
savings_account_1.deposit(1000)
savings_account_1.withdraw(500)
print(savings_account_1.balance)
savings_account_1.withdraw(1500)
