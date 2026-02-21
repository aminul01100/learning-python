"""
* Problem statement:
build an ATM machine system, that will provide the following functionalities for only one user-
    - Cash withdrawal
    - Cash deposit
    - Transfer money to another account
    - Check balance
"""

"""
Solution Steps:
1. take input for pin number and validate it
2. show action list to user
3. take input from user and validate it
    a. cash withdrawal:
        - take input for amount to withdraw and validate (check if balance is sufficient or not) it
        - withdraw cash and update balance
    b. cash deposit:
        - take input for amount to deposit and validate it (maximum deposit limit is 50000)
        - add deposited amount to balance
    c. Transfer money to another account
        - take input for account number and bank name and validate it (check if account number is 12 digit or not)
        - take input for transfer amount validate it (check if balance is sufficient or not)
        - deduct transfer amount from balance
    d. Check balance:
        - show balance and current date to user
"""

TAJ_BHAI_ER_PIN = 1234
CURRENT_BALANCE = 1000000

while True:
    # 1. take input for pin number and validate it
    user_pin = input("Enter your pin number: ")
    user_pin = int(user_pin) # type casting to int from str

    if user_pin != TAJ_BHAI_ER_PIN:
        print("Invalid pin number, try again")
        continue
    
    print("Welcome to Taj Bhai's ATM machine")

    # 2. show action list to user
    print("1. Cash withdrawal")
    print("2. Cash deposit")
    print("3. Transfer money to another account")
    print("4. Check balance")

    # 3. take input from user and validate it
    while True:
        user_action = input("Select an action (1-4): ")
        user_action = int(user_action) # type casting to int from str
        if user_action < 1 or user_action > 4:
            print("Invalid action, try again")
        else:
            break
    
    # 4. define what will be done for the selected action
    if user_action == 1:
        while True:
            withdrawal_amount = input("Enter amount to withdraw: ")
            withdrawal_amount = int(withdrawal_amount) # type casting to int from str

            if withdrawal_amount > CURRENT_BALANCE:
                print("Insufficient balance, try again")
            elif withdrawal_amount <= 0:
                print("Invalid amount, try again")
            elif withdrawal_amount > 50000:
                print("Maximum withdrawal limit is 50000, try again")
            elif withdrawal_amount == CURRENT_BALANCE:
                print("You cannot withdraw all your money, try again")
            else:
                CURRENT_BALANCE = CURRENT_BALANCE - withdrawal_amount
                print("Cash withdrawn successfully, your current balance is: ", CURRENT_BALANCE)
                break
        continue
    elif user_action == 2:
        while True:
            deposit_amount = input("Enter amount to deposit: ")
            deposit_amount = int(deposit_amount) # type casting to int from str
            if deposit_amount <= 1000 or deposit_amount > 50000:
                print("Invalid amount, should be between 1000 and 50000, try again")
            
            else:
                CURRENT_BALANCE = CURRENT_BALANCE + deposit_amount
                print("Cash deposited successfully, your current balance is: ", CURRENT_BALANCE)
                break
        continue
    
        