import matplotlib.pyplot as plt

class ATM:
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance
        self.authenticated = False
        self.withdraw_history = []
        self.balance_history = []

    def verify_pin(self, entered_pin):
        if entered_pin == self.pin:
            self.authenticated = True
            print("\n✅ PIN Verified Successfully!")
            return True
        else:
            print("\n❌ Incorrect PIN.")
            return False

    def withdraw(self, amount):
        if not self.authenticated:
            print("Please authenticate first.")
            return

        if amount > self.balance:
            print(f"❌ Insufficient funds! Current balance: ${self.balance}")
        elif amount <= 0:
            print("❌ Invalid amount.")
        else:
            self.balance -= amount
            print(f"✅ Withdrawal Successful! Dispensed: ${amount}")
            print(f"💰 Remaining Balance: ${self.balance}")

            # Save data for graph
            self.withdraw_history.append(amount)
            self.balance_history.append(self.balance)

    def show_graph(self):
        if len(self.withdraw_history) == 0:
            print("No transactions to display graph.")
            return

        plt.plot(self.withdraw_history, self.balance_history, marker='o')
        plt.xlabel("Withdrawal Amount")
        plt.ylabel("Remaining Balance")
        plt.title("ATM Withdrawal Graph")
        plt.grid()
        plt.show()


# -------- MAIN PROGRAM --------
def main():
    atm = ATM(pin=1234, balance=1000)

    print("🏧 --- Welcome to ATM ---")
    entered_pin = int(input("Enter your PIN: "))

    if atm.verify_pin(entered_pin):
        while True:
            print("\n1. Withdraw Money")
            print("2. Show Graph")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                amount = int(input("Enter amount to withdraw: "))
                atm.withdraw(amount)

            elif choice == "2":
                atm.show_graph()

            elif choice == "3":
                print("🙏 Thank you for using ATM")
                break

            else:
                print("❌ Invalid choice")

    else:
        print("🚫 Access Denied")


# Run the program
if __name__ == "__main__":
    main()
