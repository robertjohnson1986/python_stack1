class BankAccount:
    def __init__(self, int_rate=0, balance=0):
        self.int_rate = int_rate 
        self.balance = balance 
        
    def deposit(self, amount):
        self.balance += amount 
        return self

    def withdraw(self, amount):
        # check the balance and see if it's greater than the amount 
        if self.balance >= amount:
            self.balance -= amount 
        else:
            self.balance -= 5 
            print("Insufficient Funds: Charging a $5 fee")
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + self.balance * self.int_rate
        return self


ba1 = BankAccount(balance=100)
ba2 = BankAccount(.01, 500)

ba1.deposit(100).deposit(50).deposit(50).withdraw(100).yield_interest().display_account_info()
ba2.deposit(100).deposit(100).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()


class User:        # here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)    # added this line
    # adding the deposit method
    def make_deposit(self, amount):    # takes an argument that is the amount of the deposit
        self.account.deposit(100)        # we can call the BankAccount instance's methods
        print(self.account.balance)        # or access its attributes
        return self

    def make_withdrawal(self, amount):
        self.account.withdrawl(100)        # we can call the BankAccount instance's methods
        print(self.account.balance)        # or access its attributes
        return self
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account.balance}")
        return self   
    
    def transfer_money(self, other_user, amount):
        # BONUS
        # let's leverage the fact that we have deposit and withdrawal methods that are available to self and other_user
        # since they're both User objects...You don't have to do it this way though.
        other_user.make_deposit(amount) # could also say other_user.account_balance += amount
        self.make_withdrawal(amount) # could also say self.account_balance -= amount
        return self


todd = User("Todd", "todd@todd.com")
jane = User("Jane", "jane@jane.com")
john = User("John", "john@john.com")

todd.make_deposit(100).make_deposit(100).make_withdrawal(50).display_user_balance()

jane.make_deposit(50).make_deposit(1000).make_withdrawal(500).make_withdrawal(100).display_user_balance()

john.make_deposit(100).make_withdrawal(25).make_withdrawal(25).make_withdrawal(25).display_user_balance()