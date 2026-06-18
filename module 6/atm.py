""" Write a simple ATM withdrawal program: take the account balance and withdrawal
amount as input, and print 'Withdrawal successful' with the new balance if funds are
sufficient, otherwise print 'Insufficient balance'. Also check that the withdrawal amount
is a multiple of 100, otherwise print an error."""
balance = int(input("Enter account balance: "))

while True:
    withdraw_amount = int(input("Enter withdrawal amount: "))

    if withdraw_amount % 100 != 0:
        print("Error: Withdrawal amount must be a multiple of 100")
    elif withdraw_amount > balance:
        print("Insufficient balance")
    else:
        balance -= withdraw_amount
        print("Withdrawal successful")
        print("New balance:", balance)

    choice = input("Do you want another transaction? (yes/no): ")

    if choice.lower() == "no":
        print("Thank you for using the ATM.")
        break