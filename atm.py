# ATM Machine Simulation

def authenticate_user(correct_pin, attempts=3):
    """
    Function to authenticate user using PIN.
    Allows limited attempts.
    """
    while attempts > 0:
        entered_pin = input("🔐 Enter your PIN: ")
        if entered_pin == correct_pin:
            print("✅ Authentication Successful\n")
            return True
        else:
            attempts -= 1
            print(f"❌ Incorrect PIN. Attempts left: {attempts}")
    
    print("🚫 Card Blocked. Too many incorrect attempts.")
    return False


def show_menu():
    """
    Displays ATM menu options.
    """
    print("\n====== ATM MENU ======")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Exit")


def check_balance(balance):
    """
    Displays current balance.
    """
    print(f"💰 Your current balance is: ₹{balance}")


def withdraw_money(balance):
    """
    Handles withdrawal operation.
    """
    try:
        amount = float(input("💸 Enter amount to withdraw: ₹"))
        
        if amount <= 0:
            print("❌ Invalid amount. Please enter a positive value.")
        elif amount > balance:
            print("❌ Insufficient balance.")
        else:
            balance -= amount
            print(f"✅ Please collect your cash: ₹{amount}")
            print(f"💰 Remaining balance: ₹{balance}")
    
    except ValueError:
        print("❌ Invalid input. Please enter a numeric value.")
    
    return balance


def atm_machine():
    """
    Main ATM function.
    """
    balance = 10000.0
    correct_pin = "1234"

    print("🏧 Welcome to ATM Machine")

    # Authenticate user
    if not authenticate_user(correct_pin):
        return

    # Main loop
    while True:
        show_menu()
        choice = input("👉 Enter your choice: ")

        if choice == "1":
            check_balance(balance)

        elif choice == "2":
            balance = withdraw_money(balance)

        elif choice == "3":
            print("🙏 Thank you for using ATM. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please try again.")


# Run the ATM system
if __name__ == "__main__":
    atm_machine()
