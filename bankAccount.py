

class BankAccount:

    def __init__(self, account_balance, int_rate): 
        self.account_balance = account_balance
        self.int_rate = int_rate

    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdraw(self, amount):
        self.account_balance -= amount
        if (self.account_balance < 0):
            print("Insufficient funds: Charging a $5 fee")
            self.account_balance -= 5
        return self

    def display_account_info(self):
        print(f"Your account balance is: {self.account_balance}")
        return self

    def yield_interest(self):
        if self.account_balance > 0:
            self.account_balance += (self.account_balance * self.int_rate)
        return self

balance1 = BankAccount(0, 0.02)
balance2 = BankAccount(0, 0.02)

balance1.deposit(100).deposit(100).deposit(100).withdraw(100).yield_interest().display_account_info()
balance2.deposit(100).deposit(100).withdraw(50).withdraw(50).withdraw(100).withdraw(5).yield_interest().display_account_info()
