class BankAccount:
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if amount > self.account_balance:
            return 1
        else:
            self.account_balance -= amount
            return 0
    def display_balance(self):
        print(f"Current balance: {self.account_balance}")