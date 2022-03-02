from BankAccount import BankAccount

class User:
    def __init__(self,name):
        self.name = name
        self.accounts = []

    def create_new_account(self):
        self.accounts.append(BankAccount(0.05,0))
        id = len(self.accounts)
        print(f'The ID of your new account is: {id}')

    def make_a_deposit(self,amount, id_account):
        self.accounts[id_account-1].balance += amount
        return self
    
    def withdraw_money(self,amount, id_account):
        self.accounts[id_account-1].balance -= amount
        return self

    def show_balance(self, id_account):
        print(f'User: {self.name}, Account ID: {id_account} ,Balance: ${self.accounts[id_account-1].balance}')
    

    
