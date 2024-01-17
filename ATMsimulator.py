class ATM:
    def __init__(self, balance=0, password="1234"):
        self.balance = balance
        self.password = password

    def authenticate(self, entered_password):
        return entered_password == self.password

    def check_balance(self):
        entered_password = input("Enter your password: ")
        if self.authenticate(entered_password):
            print(f"Current Balance: ${self.balance}")
        else:
            print("Authentication failed.")

    def deposit(self):
        entered_password = input("Enter your password: ")
        if self.authenticate(entered_password):
            amount = float(input("Enter the deposit amount: $"))
            self.balance += amount
            print(f"Deposit successful. New Balance: ${self.balance}")
        else:
            print("Authentication failed.")

    def withdraw(self):
        entered_password = input("Enter your password: ")
        if self.authenticate(entered_password):
            amount = float(input("Enter the withdrawal amount: $"))
            if self.balance - amount < 100:
                print("Withdrawal not allowed. Minimum balance should be $100.")
            else:
                self.balance -= amount
                print(f"Withdrawal successful. Remaining Balance: ${self.balance}")
        else:
            print("Authentication failed.")

    def change_password(self):
        entered_password = input("Enter your current password: ")
        if self.authenticate(entered_password):
            new_password = input("Enter new password: ")
            self.password = new_password
            print("Password changed successfully.")
        else:
            print("Authentication failed.")


def main():
    # Creating an instance of the ATM class
    atm = ATM(balance=500)

    while True:
        print("\n=== ATM Simulator ===")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change Password")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            atm.deposit()
        elif choice == "3":
            atm.withdraw()
        elif choice == "4":
            atm.change_password()
        elif choice == "5":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
