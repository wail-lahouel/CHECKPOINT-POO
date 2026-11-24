# ==========================================================
# BANK ACCOUNT PROJECT
# File name: bank_account.py
# Objective: Simulate basic bank account operations using OOP
# ==========================================================

# 1. Create the Account class
class Account:

    # 2. Constructor: initialize the account attributes
    def __init__(self, account_number, account_holder, balance=0.0):

        # Account attributes
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    # 3. Deposit method
    def deposit(self, amount):

        # Check if the amount is positive
        if amount <= 0:
            print("Error: Deposit amount must be positive.")
            return

        # Add the amount to the current balance
        self.balance += amount

        print(f"{amount:.2f} DA deposited successfully.")

    # 4. Withdraw method
    def withdraw(self, amount):

        # Check if the amount is positive
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return

        # Check if there is enough money in the account
        if self.balance >= amount:

            # Subtract the amount from the balance
            self.balance -= amount

            print(f"{amount:.2f} DA withdrawn successfully.")

        else:
            print("Error: Insufficient balance.")

    # 5. Check balance method
    def check_balance(self):

        # Return the current balance
        return self.balance

    # 6. Display account information
    def display_account(self):

        print("\n========== ACCOUNT INFORMATION ==========")
        print(f"Account number : {self.account_number}")
        print(f"Account holder : {self.account_holder}")
        print(f"Balance        : {self.balance:.2f} DA")
        print("=======================================")


# ==========================================================
# 7. Create the first account
# ==========================================================

mon_compte = Account("00123456", "Khelil", 1000.0)

# Display initial account information
mon_compte.display_account()


# ==========================================================
# 8. Perform transactions on the first account
# ==========================================================

print("\n--- Transactions for mon_compte ---")

# Deposit 500 DA
mon_compte.deposit(500)

# Withdraw 200 DA
mon_compte.withdraw(200)

# Try to withdraw more money than available
mon_compte.withdraw(2000)

# Check the balance
print(f"Current balance: {mon_compte.check_balance():.2f} DA")


# ==========================================================
# 9. Create a second account
# ==========================================================

compte_2 = Account("00234567", "Ahmed", 5000.0)

# Display second account information
compte_2.display_account()


# ==========================================================
# 10. Perform transactions on the second account
# ==========================================================

print("\n--- Transactions for compte_2 ---")

# Deposit 1500 DA
compte_2.deposit(1500)

# Withdraw 1000 DA
compte_2.withdraw(1000)

# Check the balance
print(f"Current balance: {compte_2.check_balance():.2f} DA")


# ==========================================================
# 11. Create a third account
# ==========================================================

compte_3 = Account("00345678", "Sara", 0.0)

# Display third account information
compte_3.display_account()


# ==========================================================
# 12. Perform transactions on the third account
# ==========================================================

print("\n--- Transactions for compte_3 ---")

# Deposit 3000 DA
compte_3.deposit(3000)

# Withdraw 500 DA
compte_3.withdraw(500)

# Check the balance
print(f"Current balance: {compte_3.check_balance():.2f} DA")


# ==========================================================
# 13. Display all final balances
# ==========================================================

print("\n========== FINAL BALANCES ==========")

print(f"{mon_compte.account_holder}: "f"{mon_compte.check_balance():.2f} DA")

print(f"{compte_2.account_holder}: "f"{compte_2.check_balance():.2f} DA")

print(f"{compte_3.account_holder}: "f"{compte_3.check_balance():.2f} DA")

print("===================================")