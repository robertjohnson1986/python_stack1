# If you've been following along, you're going to utilize the 
# User class we've been discussing for this assignment.

# For this assignment, we'll add some functionality to the User class:

# make_withdrawal(self, amount) - have this method decrease the user's 
# balance by the amount specified
# display_user_balance(self) - have this method print the user's name 
# and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
# BONUS: transfer_money(self, other_user, amount) - have this method 
# decrease the user's balance by the amount and add that amount to 
# other other_user's balance
# Create a file with the User class, including the __init__ and 
# make_deposit methods  Add a make_withdrawal method to the User class
# Add a display_user_balance method to the User class  Create 3 instances
# of the User class  Have the first user make 3 deposits and 1 withdrawal
# and then display their balance  Have the second user make 2 deposits 
# and 2 withdrawals and then display their balance  Have the third user 
# make 1 deposits and 3 withdrawals and then display their balance  
# BONUS: Add a transfer_money method; have the first user transfer money 
# to the third user and then print both users' balances
class User:        # here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):    # takes an argument that is the amount of the deposit
        self.account_balance += amount    # the specific user's account increases by the amount of the value received.
        return self
    def make_withdrawl(self, amount): #takes an argument that is the amount of the withdrawl
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print("User:",self.name,", Balance: ", self.account_balance)
        return self
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
robert = User("Robert Johnson", "kuyperhouse@gmail.com")
print(guido.name)    # output: Guido van Rossum
print(monty.name)    # output: Monty Python
print(robert.name)
guido.make_deposit(100).make_deposit(200).make_deposit(100).make_deposit(300).make_withdrawl(1).display_user_balance()
monty.make_deposit(50).make_withdrawl(1).make_withdrawl(56.22).make_withdrawl(28.69).display_user_balance()
robert.make_deposit(6000).make_withdrawl(1).make_withdrawl(2.33).display_user_balance()
print(guido.account_balance)    # output: 300
print(monty.account_balance)    # output: 50
print(robert.account_balance)