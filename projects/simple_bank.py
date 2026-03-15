# Simple Bank Account System
class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self._balance = balance
        self._transactions = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        self._transactions.append(("deposit", amount))
        return self._balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        self._transactions.append(("withdrawal", amount))
        return self._balance

    @property
    def balance(self):
        return self._balance

    def statement(self):
        print(f"\nAccount: {self.owner}")
        print(f"Balance: ${self._balance:.2f}")
        print("Transactions:")
        for t_type, amount in self._transactions:
            print(f"  {t_type}: ${amount:.2f}")

account = BankAccount("Habtamu", 1000.0)
account.deposit(500)
account.withdraw(200)
account.statement()
