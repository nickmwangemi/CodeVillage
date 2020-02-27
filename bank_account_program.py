def print_menu():
    print("1. List Account(s)")
    print("2. Open an Account")
    print("3. Close an Account")
    print("4. Withdraw money")
    print("5. Deposit Money")
    print("6. Quit")
    print()


accounts = {}
menu_choice = 0
print_menu()
# balance = {}
balance = 0
while True:
    menu_choice = int(input("Type in a number (1-6): "))
    print

    if menu_choice == 1:
        print("Accounts")
        for x in accounts.keys():
            print("\nAccount Number:", x, "with balance KSh.", balance)
            print("\n{} {} Acc No.: {}, balance: {} ".format(
                firstName, lastName, x, balance))
        print

    elif menu_choice == 2:
        print("Create a new account: ")
        firstName = input("Please enter the first name: ")
        accounts[firstName] = firstName
        lastName = input("Please enter the last name: ")
        accounts[lastName] = lastName
        mobileNumber = input("Please enter the mobile number: ")
        accounts[mobileNumber] = mobileNumber
        # unique customer
        # isUnique = input()
        number = input("New Account Number: ")
        # phone = input("Number: ")
        accounts[number] = number
        print("Account Number", number, "opened.")
    elif menu_choice == 3:
        print("Close an Account Number")
        number = input("Account Number: ")
        if number in accounts:
            # accounts[number]=balance
            del accounts[number]
            print("Account Number", number, "is closed.")
        else:
            print("Account Number", number, "was not found")
    # elif menu_choice == 4:
        # print(("Lookup Number")
        # name = input("Name: ")
        # if name in numbers:
        #    print(("The number is", numbers[name])
        # else:
        #    print((name, "was not found")
    elif menu_choice == 4:
        print("Withdraw money from Account.")
        number = input("Account Number: ")
        if number in accounts:
            withdraw = float(
                input("How much money would you like to withdraw? "))
            balance = accounts[number]
            if withdraw < balance:
                accounts[number] -= withdraw
                print("Your new balance is Ksh.", accounts[number])
            else:
                print("Sorry. Insufficient funds.")
    elif menu_choice == 5:
        print("Deposit money into account.")
        number = input("Account Number: ")
        if number in accounts:
            deposit = float(
                input("How much money would you like to deposit? "))
            # accounts[number]=balance
            balance += deposit
            # balance
            print("Your new balance is Ksh.", balance)
        else:
            print("That account number does not exist.")
    elif menu_choice == 6:
        print("Quit.")
        break
    else:
        print("Please enter a number between 1 and 6.")
    print()
    print_menu()
