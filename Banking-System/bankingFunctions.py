from customerClass import Customer
from accountClass import Account
from currencyClass import Currency


def intro():
    print("\t\t\t\t**********************")
    print("\t\t\t\tWelcome to Pesa Chap Chap")
    print("\t\t\t\t**********************")


def checkBalance():
    customers = []

    customer1 = Customer("Nick M.", "32020690", "pesachap001", "254722010101", "1234", Account(
        "Jijenge", "savings", 5000, Currency("KES", "Kenya Shillings", "Ksh.")))

    customer2 = Customer("John Doe", "34250690", "pesachap002", "254722020202", "5678", Account(
        "Jijenge", "savings", 1000, Currency("KES", "Kenya Shillings", "Ksh.")))

    customer3 = Customer("Jane Doe", "35692490", "pesachap003", "254722030303", "9112", Account(
        "Jijenge", "savings", 3000, Currency("KES", "Kenya Shillings", "Ksh.")))

    # Customer is an object. Create an instance of a customer then append to customers list
    customers.append(customer1)
    customers.append(customer2)
    customers.append(customer3)

    # statements for all customers
    for cust in customers:
        print("\nName: {} ID No.: {} Customer Number: {} Mobile No: {}  PIN: {} \nAccount: {} Type: {} Balance: {} Currency Code: {} Currency Name: {} Currency Short Name: {}".format(
            cust.name, cust.idNo, cust.customerNo, cust.phoneNumber, cust.pin,
            cust.account.accountName, cust.account.accountType, cust.account.balance,
            cust.account.currency.code, cust.account.currency.name, cust.account.currency.shortName
        ))
    print("*"*50)

    # balance for one customer
    phoneNumber = input("Please enter your phone number: ")
    for cust in customers:
        if phoneNumber in cust.phoneNumber:
            print("\nDear {} of {}, Your balance is: {} {}".format(
                cust.name, cust.phoneNumber, cust.account.currency.shortName, cust.account.balance))
    print("*"*50)
    # exit to main menu
    exitToMain = int(input("Press 0 to exit to main menu "))
    if exitToMain == 0:
        intro()  # call main menu function


def sendMoney():
    customers = []

    customer1 = Customer("Nick M.", "32020690", "pesachap001", "254722010101", "1234", Account(
        "Jijenge", "savings", 5000, Currency("KES", "Kenya Shillings", "Ksh.")))

    customer2 = Customer("John Doe.", "34250690", "pesachap002", "254722020202", "5678", Account(
        "Jijenge", "savings", 1000, Currency("KES", "Kenya Shillings", "Ksh.")))

    customer3 = Customer("Jane Doe", "35692490", "pesachap003", "254722030303", "9112", Account(
        "Jijenge", "savings", 3000, Currency("KES", "Kenya Shillings", "Ksh.")))

    # Customer is an object. Create an instance of a customer then append to customers list
    customers.append(customer1)
    customers.append(customer2)
    customers.append(customer3)

    phoneNumber = input("Please enter your phone number: ")
    # check if phone exists in customers list
    for cust in customers:
        if phoneNumber in cust.phoneNumber:
            amount = float(input("Enter the amount: "))
            # check if balance > amount
            if amount > cust.account.balance:
                print("\nSorry. You have insufficient funds. Please top up.")
                # exit to main menu
                intro()
            elif cust.account.balance >= amount:
                recPhoneNumber = input("Enter the recipient's phone number: ")
                # check if recipients number is in customer list
                for cust in customers:
                    if recPhoneNumber in cust.phoneNumber:
                        pin = (input("Please enter your PIN: "))
                        # validate pin
                        for cust in customers:
                            if pin in cust.pin:
                                confirm = int(input("Press '1' to proceed "))
                                if(confirm == 1):
                                    newBal = cust.account.balance - amount
                                    for cust in customers:
                                        print("\nDear {}, {} {} has been sent to {}({}). Your balance is {}{}".format(
                                            cust.name, cust.account.currency.shortName, amount, cust.name, recPhoneNumber, cust.account.currency.shortName, newBal))
                                        exitToMain = int(
                                            input("Press 0 to exit to main menu "))
                                        if exitToMain == 0:
                                            intro()  # call main menu function
