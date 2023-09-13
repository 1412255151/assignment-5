class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

title = input("Enter account Type: ")
balance = float(input("Enter account balance: "))
account = Account(title, balance)

title = input("Enter savings account user name : ")
balance = float(input("Enter savings account balance: "))
interest_rate = float(input("Enter savings account interest rate: "))
savings_account = SavingsAccount(title, balance, interest_rate)

print("\nAccount Details:")
print(f"Title: {account.title}")
print(f"Balance: {account.balance}")

print("\nSavings Account Details:")
print(f"user name : {savings_account.title}")
print(f"Balance: {savings_account.balance}")
print(f"Interest Rate: {savings_account.interestRate}%")