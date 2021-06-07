class BankAccount:
    def __init__(self, int_rate=0, balance=0):
        self.int_rate = int_rate 
        self.balance = balance 
        
    def deposit(self, amount):
        self.balance += amount 
        return self

    def withdrawl(self, amount):
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

class User:        # here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)    # added this line
    # adding the deposit method
    def make_deposit(self, amount):    # takes an argument that is the amount of the deposit
        self.account.deposit(amount)        # we can call the BankAccount instance's methods
        print(self.account.balance)        # or access its attributes
        return self

    def make_withdrawal(self, amount):
        self.account.withdrawl(amount)        # we can call the BankAccount instance's methods
        print(self.account.balance)        # or access its attributes
        return self
    
    def display_user_balance(self):
        self.account.display_account_info()
        return self   
    
    def transfer_money(self, other_user, amount):
        # BONUS
        # let's leverage the fact that we have deposit and withdrawal methods that are available to self and other_user
        # since they're both User objects...You don't have to do it this way though.
        other_user.make_deposit(amount) # could also say other_user.account_balance += amount
        self.make_withdrawal(amount) # could also say self.account_balance -= amount
        return self


robert = User("Robert", "rjenglish@gmail.com")

robert.make_deposit(50).make_deposit(100).make_withdrawal(50).display_user_balance()
robert.account.yield_interest()
robert.display_user_balance()
robert.account.display_account_info()
