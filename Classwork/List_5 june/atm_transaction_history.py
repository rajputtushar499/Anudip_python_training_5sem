# Store all transactions in a list
transactions = [5000, -2000, 3000, -1000, -500, 7000]

# Variable to store current balance
balance = 0

# Empty list to store deposits
deposits = []

# Empty list to store withdrawals
withdrawals = []

# Loop through each transaction
for amount in transactions:

    # Add transaction amount to balance
    balance = balance + amount

    # Check if transaction is a deposit
    if amount > 0:

        # Add deposit amount to deposits list
        deposits.append(amount)

    # Otherwise it is a withdrawal
    else:

        # Add withdrawal amount to withdrawals list
        withdrawals.append(amount)

# Assume first deposit is the largest deposit
largest_deposit = deposits[0]

# Assume first withdrawal is the largest withdrawal
largest_withdrawal = withdrawals[0]

# Loop through deposits list
for amount in deposits:

    # Check if current deposit is greater
    if amount > largest_deposit:

        # Update largest deposit
        largest_deposit = amount

# Loop through withdrawals list
for amount in withdrawals:

    # Check if current withdrawal is smaller (more negative)
    if amount < largest_withdrawal:

        # Update largest withdrawal
        largest_withdrawal = amount

# Display current balance
print("Current Balance:", balance)

# Display all deposits and withdrawals
print("Deposits:", deposits)
print("Withdrawals:", withdrawals)
print("Largest Deposit:", largest_deposit)
print("Largest Withdrawal:", largest_withdrawal)
