class Account:
    def __init__(self, initial_balance=0.0):
        self.balance = initial_balance

    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdrawal(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount


class SavingsAccount(Account):
    def interestAmount(self, rate):
        if rate > 0:
            return self.balance * (rate / 100)
        else:
            return 0


# Create a new SavingsAccount object
initial_balance = float(input("Enter the initial balance for your Savings Account: "))
savings_account = SavingsAccount(initial_balance)

while True:
    print("\nChoose an action:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Calculate Interest Amount")
    print("5. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print(f"Your balance is: {savings_account.getBalance()}")
    elif choice == 2:
        amount = float(input("Enter the amount to deposit: "))
        savings_account.deposit(amount)
        print(f"Deposited {amount} successfully.")
        print(f"Total amount :{amount+initial_balance} = ")
    elif choice == 3:
        amount = float(input("Enter the amount to withdraw: "))
        savings_account.withdrawal(amount)
        print(f"Withdrew {amount} successfully.")
        print(f"Total amount {initial_balance-amount} = ")
    elif choice == 4:
        rate = float(input("Enter the interest rate (%): "))
        interest = savings_account.interestAmount(rate)
        print(f"Interest Amount per/month : {interest}")
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please choose a valid option.")

print("Thank you for using our banking system!")
