class Account:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

# create a deposit method
    def deposit(self, amount):
        self.balance += amount
        print(f'{self.name} Deposited {amount} $. Currente Balance is: {self.balance}')

# create a withdraw method
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f'{self.name} Withdrew {amount} $. Current Balance is: {self.balance}')
        else:
            print("You don't have enough funds to withdraw.")

# Inheritance works
class Savings_Account(Account):
    def __init__(self, name, account_number, balance, interest_rate):
        super().__init__(name, account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)

account1 = Account("John Doe", "123456", 1000)
account1.deposit(500)
account1.withdraw(200)
print()

savings_account = Savings_Account("John Doe", "789012", 2000, 0.05)
savings_account.deposit(1000)
savings_account.add_interest()
savings_account.withdraw(500)
savings_account.withdraw(1000)  