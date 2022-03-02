class BankAccount:
    all_accounts =[]
  
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw_money(self, amount):
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            print(f'Insufficient funds')
        return self
        
    def show_account_info(self):
        print(f'Balance: ${self.balance}')

    def generate_int(self):
        if BankAccount.is_balance_positive(self.balance):
            self.balance += (self.balance*self.int_rate)

        return self

    @staticmethod
    def can_withdraw(balance,ammount_to_withdraw):
        if balance > ammount_to_withdraw:
            return True
        else:
            return False

    @staticmethod
    def is_balance_positive(balance):
        return balance > 0

    @classmethod
    def print_account(cls):
        for account in cls.all_accounts:
            account.show_all_account_info()

    def show_all_account_info(self):
        print(f'Interest Rate: {self.int_rate}, Balance: {self.balance}')
