'''
Objectives: 
- Welcome Message: The program starts by greeting the user, setting the stage for ATM simulation.
- Initialize Amount Balance: The balance variable is set to 1000, representing the user's starting account balance.
- Set Up and verify PIN
- user choice is captured through input and handled
'''

def main():
    print("Welcome to ATM simulation")
    pin()
    print("Thank you for banking with us")

def pin():
    correct_pin = "1234"
    atm_on = False
    entered_pin = input("Enter your pin: ")
    
    if entered_pin == correct_pin:
        atm_on = True
        menu()
    else:
        atm_on = False
        print("Please, Enter your correct pin")
        pin()
        
    return(atm_on)

def menu():
    acc_balance = 1000
    print("\nWhat would you like to do today? \n1. Check Balance \n2. Deposit Money \n3. Withdraw Money \n4. Exit")
    user_choice = input("Enter your choice: ")

    if user_choice == "1" or user_choice.lower == "check balance":
        print("Your account balance is ", end = " ")
        balance(acc_balance)
    elif user_choice == "2" or user_choice.lower =="deposit money":
        deposit(acc_balance)
    elif user_choice == "3" or user_choice.lower == "withdraw money":
        withdraw(acc_balance)
    elif user_choice == "4" or user_choice.lower == "exit":
        print("Thank you for banking with us")
        exit()
    else:
        print("Incorrect choice")
        menu()

def balance(acc_balance):
    print(acc_balance)

def deposit(acc_balance):
    deposit_amount = int(input("How much would you like to deposit: "))
    acc_balance += deposit_amount
    print(f"You deposited {deposit_amount}, your balance is now {acc_balance}")

def withdraw(acc_balance):
    withdraw_amount = int(input("How much would you like to withdraw: "))
    if withdraw_amount < acc_balance:
        acc_balance -= withdraw_amount
        print(f"You just withdrawed {withdraw_amount}, your balance is now {acc_balance}")
    else:
        print("Your balance is insufficient")


main()
