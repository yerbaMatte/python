from bank_account import *

Dave = BankAccount(1000, 'Dave')
Sara = BankAccount(2000, 'Sara')

Dave.getBalance()
Sara.getBalance()

Sara.deposit(500)

Dave.withdraw(10000)
