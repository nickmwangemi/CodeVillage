# start of the program
from bankingFunctions import checkBalance
from bankingFunctions import sendMoney
from bankingFunctions import intro

choice = 0
while choice != 2:
    intro()
    # system("cls");
    print("\tMAIN MENU")
    print("\t1. Check Balance")
    print("\t2. Send Money")

    print("\t3. EXIT")
    print("\tSelect Your Option (1-3) ")
    choice = input()

    if choice == '1':
        checkBalance()
    elif choice == '2':
        sendMoney()
    elif choice == '3':
        print("\tThanks for using our system")
        break
    else:
        print("Invalid choice")
        choice = int(input("Please select an option between 1-3 : "))
        while choice > 3:
            choice = int(input("Please select an option between 1-3 : "))
