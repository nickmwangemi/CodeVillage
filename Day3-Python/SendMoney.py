recipientName = input("Enter name of recipient:")
recipientPhone = input("Enter phone number:")
amount = int(input("Enter amount:"))

print("Send {} to {} of {}".format(amount, recipientName, recipientPhone))

confirm = int(input("Press '1' to proceed "))
if(confirm == 1):
    balance = 3000
    # transaction fee of 1%
    newBal = 3000 - (amount + (0.01*amount))


print("Confirmed {} sent to {} of {}. Balance is {}".format(
    amount, recipientName, recipientPhone, newBal))

# check mobile number
if "254" not in recipientPhone:
    print("Please enter the phone in the format of 254xxxxxxxx")

# amount not more than balance
if amount > balance:
    print("Sorry. You have insufficient funds. Please top up.")


"""
validations- mobile number, amount not more than balance, transaction fee of 1%
"""
