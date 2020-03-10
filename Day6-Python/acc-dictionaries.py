# multiple customers
customers = {}
accBalance = 0
deposit = 0
# no of customers
noOfCustomers = int(input('How many customers would you like to add? '))

# input details for many customers
for n in range(1, noOfCustomers+1):
    customer = {}
    firstName = input('Enter First Name: ')
    customer['firstName'] = firstName

    lastName = input('Enter Last Name: ')
    customer['lastName'] = lastName

    mobileNo = input('Enter Mobile Number: ')
    customer['mobileNo'] = mobileNo

    idNo = input('Enter ID Number: ')
    customer['idNo'] = idNo

    customerID = input('Enter unique customer ID: ')
    customer['customerID'] = customerID

    accountType = input(
        'Enter the type of account: Savings or Current? ').lower()
    customers['accountType'] = accountType

    # account type
    if accountType == 'savings':
        print("You chose a {} account".format(accountType))
        deposit = int(
            input("Enter the account opening balance (>=500 for Savings and >=1000 for Current) "))

    elif accountType == 'current':
        print("You chose a {} account".format(accountType))
        deposit = int(
            input("Enter the account opening balance (>=500 for Savings and >=1000 for Current) "))

    # account number
    accNo = input("Enter the account number: ")
    customers['accNo'] = accNo

    # currency
    currency = input(
        "Enter the currency that the account will operate in: KES or USD? ").lower()
    if currency == 'usd' or 'kes':
        customers['currency'] = currency

print(customers)
# account balance
# accBalance += deposit
# customers['accBalance'] = accBalance


print("\n****Account Created****")


# print("\t\t\t\t**********************")
# print("\t\t\t\tBANK MANAGEMENT SYSTEM")
# print("\t\t\t\t**********************")

# print("\t\t\t\tBrought To You By:")
# print("\t\t\t\tBANKIKA")

print("\n\n{} {}".format(firstName, lastName))
print("Mobile No: {} ID No: {}".format(mobileNo, idNo))
print("Customer ID: {} Account Type: {} Acc No: {} Balance: {}" .format(
    customerID, accountType, accNo, accBalance))
print("Account Balance: {}".format(accBalance))
