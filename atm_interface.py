class ATM:
    def __init__(self, balance=5000):  

        
        self.balance = balance

    def check_balance(self):
        print("--------------------------------------")
        print(f"Your current balance is: {self.balance}")
        print("--------------------------------------")


    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited successfully!")
            print(f"Your updated balance is: {self.balance}")
        else:
            print("Invalid amount! Please enter a positive number.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} is debited from your account.")

            print("---------------------------------------------")
            print(f"Your updated balance is: {self.balance}")
        elif amount > self.balance:
            print("Insufficient funds!")

            print("--------------------------------------------")
        else:
            print("Invalid amount! Please enter a positive number.")

    def exit_atm(self):
        print("Thank you for using the ATM. Goodbye!")
        print("-----------------------------------------")

def atm_interface():
    print("Please Insert Your Card")
    print("-------------------------------------------")
    pin = input("Enter Your ATM Pin: ")
    
    if pin == "1234":  
        atm = ATM()  
        while True:
            print("\n        1 == Balance")
            print("        2 == Withdraw Money")
            print("        3 == Deposit Money")
            print("        4 == Exit")


            print("------------------------------------------")

            try:
                print("----------------------------------------")
                choice = int(input("\nPlease enter your choice: "))
                print("------------------------------------------------")
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 4.")
                continue

            if choice == 1:
                atm.check_balance()
            elif choice == 2:
                try:
                    amount = float(input("Enter the amount to withdraw:"))
                    atm.withdraw(amount)
                except ValueError:
                    print("Invalid amount! Please enter a valid number.")

                    print("-----------------------------------------------------")
            elif choice == 3:
                try:
                    amount = float(input("Enter the amount to deposit:"))
                    atm.deposit(amount)
                except ValueError:
                    print("Invalid amount! Please enter a valid number.")
                    print("---------------------------------------------")
            elif choice == 4:
                atm.exit_atm()
                break
            else:
                print("Invalid choice! Please select a valid option.")
                print("--------------------------------------------")
    else:
        print("Invalid PIN! Please try again.")
        print("-----------------------------------------------")

if __name__ == "__main__":
    atm_interface()
