def atm():
    # Initialize the user's balance
    balance = 1000  # Starting balance in Ksh

    while True:
        # Present the user with a menu of options
        print("\nATM Menu")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        # Get the user's choice
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            # Check balance
            print(f"Your current balance is: Ksh.{balance}")
        
        elif choice == '2':
            # Deposit money
            amount = float(input("Enter the amount to deposit: Ksh."))
            if amount > 0:
                balance += amount
                print(f"Ksh.{amount} has been deposited. New balance is: Ksh.{balance}")
            else:
                print("Invalid amount. Please enter a positive number.")
        
        elif choice == '3':
            # Withdraw money
            amount = float(input("Enter the amount to withdraw: Ksh."))
            if amount > 0:
                if amount <= balance:
                    balance -= amount
                    print(f"Ksh.{amount} has been withdrawn. New balance is: Ksh.{balance}")
                else:
                    print("Insufficient funds. Transaction declined.")
            else:
                print("Invalid amount. Please enter a positive number.")
        
        elif choice == '4':
            # Exit
            print("Thank you for using the ATM. Goodbye!")
            break
        
        else:
            # Invalid choice
            print("Invalid choice. Please enter a number between 1 and 4.")

# Run the ATM program
if __name__ == "__main__":
    atm()
