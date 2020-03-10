# multiple customers
customers = {}

# no of customers
noOfCustomers = int(input('Enter the no of customers'))

# input details for many customers
for n in range(1, noOfCustomers+1):
    customer = {}
    firstName = input('Enter First Name: ')
    customer['firstName'] = firstName

    lastName = input('Enter Last Name: ')
    customer['lastName'] = lastName

    mobileNo = input('Enter Mobile Number:')
    customer['mobileNo'] = mobileNo
    customerID = input('Enter unique customer ID: ')
    customer['customerID'] = customerID
    accountType = input('Enter the type of account: Savings or Current? ')
    customer['accountType'] = accountType
