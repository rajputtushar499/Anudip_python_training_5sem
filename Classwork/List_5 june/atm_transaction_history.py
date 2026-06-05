# List of all transactions
transactions = [5000, -2000, 3000, -1000, -500, 7000]

# Current balance
balance = 0

# Deposit list
deposits = []

# Withdrawal list
withdrawals = []

# Check every transaction
for amount in transactions:

    # Add amount to balance
    balance += amount

    # If amount is positive, it is a deposit
    if amount > 0:
        deposits.append(amount)

    # Otherwise, it is a withdrawal
    else:
        withdrawals.append(amount)

# Find largest deposit
largest_deposit = max(deposits)

# Find largest withdrawal
largest_withdrawal = min(withdrawals)

# Print results
print("Current Balance:", balance)
print("Deposits:", deposits)
print("Withdrawals:", withdrawals)
print("Largest Deposit:", largest_deposit)
print("Largest Withdrawal:", largest_withdrawal)
