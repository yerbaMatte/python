class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = float(initialAmount)
        self.name = acctName
        print(f"\n Account '{self.name}' created. \n Balance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\nDeposit Complete.")
        self.getBalance()

    def viableTranscation(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"Sorry, account '{self.name}' only has a balance of ${self.balance:.2f}")

    def withdraw(self, amount):
        try:
            self.viableTranscation(amount)
            self.balance = self.balance - amount
            print('Withdraw Complete.')
            self.getBalance()
        except BalanceException as error:
            print(f"Withdraw interrupted. {error}")
