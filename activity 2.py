# Case Study 2: ATM Transaction Sequence Simulation
# PDF Topic No. 13

WITHDRAWAL_LIMIT = 10000

balance = float(input("Enter opening balance: "))
transaction_count = int(input("Enter number of transactions: "))

if balance < 0 or transaction_count < 0:
    print("Invalid opening balance or transaction count.")
else:
    successful_deposits = 0
    successful_withdrawals = 0
    rejected_transactions = 0
    total_deposited = 0.0
    total_withdrawn = 0.0

    for transaction_number in range(1, transaction_count + 1):
        print("\nTransaction", transaction_number)
        transaction_type = input("Enter D for deposit or W for withdrawal: ").strip().upper()
        amount = float(input("Enter transaction amount: "))

        if amount <= 0:
            print("Rejected: amount must be greater than zero.")
            rejected_transactions += 1

        elif transaction_type == "D":
            balance += amount
            total_deposited += amount
            successful_deposits += 1
            print("Deposit successful.")

        elif transaction_type == "W":
            if amount > WITHDRAWAL_LIMIT:
                print("Rejected: amount exceeds the per-transaction withdrawal limit.")
                rejected_transactions += 1
            elif amount > balance:
                print("Rejected: insufficient balance.")
                rejected_transactions += 1
            else:
                balance -= amount
                total_withdrawn += amount
                successful_withdrawals += 1
                print("Withdrawal successful.")

        else:
            print("Rejected: invalid transaction type.")
            rejected_transactions += 1

        print("Current balance: Rs.", round(balance, 2))

    print("\n--- Transaction Summary ---")
    print("Successful deposits:", successful_deposits)
    print("Successful withdrawals:", successful_withdrawals)
    print("Rejected transactions:", rejected_transactions)
    print("Total amount deposited: Rs.", round(total_deposited, 2))
    print("Total amount withdrawn: Rs.", round(total_withdrawn, 2))
    print("Final balance: Rs.", round(balance, 2))