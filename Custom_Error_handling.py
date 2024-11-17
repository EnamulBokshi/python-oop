class InsufficientFundsError(Exception):
    def __init__(self,message):
        super().__init__(message)

class BankAccount:
    def __init__(self,balance,min_balance):
        self.balance = balance
        self.min_balance = min_balance
    def withdraw(self,amount):
        current_balance = self.balance-amount
        if current_balance<self.min_balance:
            raise InsufficientFundsError('Insufficient Balance')
        print("Withdraw successful!")
        self.balance -= amount
try:
    account= BankAccount(100,20)
    account.withdraw(80)
    account.withdraw(80)
except InsufficientFundsError as err:
    print(err)



