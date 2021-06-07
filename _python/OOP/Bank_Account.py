class BankAccount:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):    # takes an argument that is the amount of the deposit
        self.account_balance += amount    # the specific user's account increases by the amount of the value received.
        return self
    def make_withdrawl(self, amount): #takes an argument that is the amount of the withdrawl
        self.account_balance -= amount
        return self
    def display_account_info(self):
        print("Balance: ", self.account_balance)
        return self
    def yield_interest(self):
        self.account_balance *= 1.1
        return self
guido = BankAccount("Guido van Rossum", "guido@python.com")
monty = BankAccount("Monty Python", "monty@python.com")
guido.make_deposit(100).make_deposit(200).make_deposit(100).make_withdrawl(1).yield_interest().display_account_info()
monty.make_deposit(50).make_deposit(5000).make_withdrawl(1).make_withdrawl(56).make_withdrawl(28).make_withdrawl(286).yield_interest().display_account_info()