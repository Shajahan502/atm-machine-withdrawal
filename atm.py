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
            print("\nPIN Verified Successfully!")
            return True
        else:
            print("\nIncorrect PIN.")
            return False

    def withdraw(self, amount):
        if not self.authenticated:
            print("Please authenticate first.")
            return

        if amount > self.balance:
            print(f"Insufficient funds! Current balance: ${self.balance}")
        elif amount <= 0:
            print("Invalid amount.")
        else:
            self.balance -= amount
            print(f"Withdrawal Successful! Dispensing: ${amount}")
            print(f"Remaining Balance: ${self.balance}")

            # Store data for graph
            self.withdraw_history.append(amount)
            self.balance_history.append(self.balance)

    def show_graph(self):
        if len(self.withdraw_history) == 0:
            print("No transactions to display graph.")
            return

        plt.plot(self.withdraw_history, self.balance_history, marker='o')
        plt.xlabel("Withdrawal Amount")
        plt.ylabel("Remaining Balance")
        plt.title("ATM Transaction Graph")
        plt.grid()
        plt.show()


# --- Simulation ---
my_atm = ATM(1234, 1000)

print("--- Welcome to the Bank ---")
pin = int(input("Enter your PIN: "))

if my_atm.verify_pin(pin):
    while True:
        print("\n1. Withdraw")
        print("2. Show Graph")
        print("3. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            amount = int(input("Enter withdrawal amount: "))
            my_atm.withdraw(amount)

        elif choice == 2:
            my_atm.show_graph()

        elif choice == 3:
            print("Thank you for using ATM!")
            break

        else:
            print("Invalid choice")

else:
    print("Transaction aborted.")
