#------------------------------------------------
# Challenge goal:
#------------------------------------------------
# For this challenge, create a bank account class 
#   that has two attributes:
#    owner
#    balance
# and two methods:
#    deposit
#    withdraw
# As an added requirement, withdrawals may not
#   exceed the available balance.
# Instantiate your class, make several 
#   deposits and withdrawals, and test to 
#   make sure the account can't be overdrawn.
#------------------------------------------------
# SEE MY CODE BELOW
#------------------------------------------------
class Account():

    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance 
    def __str__(self):
        pass
        return f"{self.owner}'s balance is {self.balance}"
    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f"Deposit Accepted. You deposited {amount}")
    def withdraw(self,amount):
        if amount > self.balance:
            print(f"Funds Unavailable! Your balance is {self.balance}")
        else: 
            self.balance = self.balance - amount
            print(f"Withdrawal Accepted. You withdrew {amount}")

# 1. Instantiate the class
acct1 = Account('Donovan',100)

# 2. Print the object
print(acct1)

# 3. Show the account owner attribute
acct1.owner

# 4. Show the account balance attribute
acct1.balance

# 5. Make a series of deposits and withdrawals
acct1.deposit(50) # Deposit Accepted

acct1.withdraw(75) # Withdrawal Accepted

# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500) # Funds Unavailable!
