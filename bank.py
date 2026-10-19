balance = 10000
attempts = 3
while True:
    if attempts == 0:
        print("You reached maximum attempts.")
        exit()
    enter_pin = int(input("Enter Pin: "))
    if enter_pin == 4567:
        while True:
            print("\n ==== Bank ====")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Exit (Enter 'q' to quit)")
            user_input = input("Input: ")
            if user_input == "q":
                exit()
            if user_input == "1":
                deposit = int(input("Deposit: "))
                if deposit <= 0:
                    print("Invalid Input")
                    continue
                else:
                    balance += deposit
                    print("Your balance:", "$", balance)
            elif user_input == "2":
                withdraw = int(input("Withdraw: "))
                if withdraw > balance:
                    print("Your balance is in the negative")
                    exit()
                else:
                    balance -= withdraw
                    print("Your balance:", "$", balance)
            else:
                print("Invalid Input")
    else:
        print("Invalid Pin")
        attempts -= 1
        print(f"Numbers of trial left {attempts}")