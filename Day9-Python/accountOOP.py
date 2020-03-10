"""
User inputs their details
Account:
- balance
- customer name
- account number
- currency
"""


class Account:
    myAccount = ""

    def __init__(self, accNo, name, balance, currency):
        self.accNo = accNo
        self.name = name
        self.balance = balance
        self.currency = currency

    def showAccount(self):
        print("Account Number : ", self.accNo)
        print("Account Holder Name : ", self.name)
        print("Balance : ", self.balance)
        print("Currency: ", self.currency)


accNo = int(input("Enter the account no : "))
name = input("Enter the account holder name : ")
balance = int(input("Enter the balance: "))
currency = input("What's the currency type? ")
print("*"*50)


myAccount = Account(accNo, name, balance, currency)
myAccount.showAccount()
