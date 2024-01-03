from random import randrange

def read_user_data():                                               #function to read all user_data and return it
    with open('Accounts.txt', 'r') as file:
        lines = file.readlines()
        user_data = [line.strip().split(',') for line in lines]
    return user_data

def update_user_data(user_data):                                    #function used to overwrite all user datas
    with open('Accounts.txt', 'w') as file:                         #with changes when the function is called
        for user in user_data:
            file.write(','.join(map(str, user)) + '\n')

def check_saved_users(username):# function to check if the user already exists according to register_user
    user_data = read_user_data()
    for user in user_data:
        if user[0] == username:
            return True

def change_user_balance(username):                                      #function to add bonus money to the account
    user_data = read_user_data()
    for user in user_data:
        if user[0] == username:
            current_balance = int(user[3])
            bonus = randrange(500, 1000)
            new_balance = current_balance + bonus
            user[3] = new_balance

    update_user_data(user_data)                             # writing new balance to the account
    print(new_balance, '$ of bonus was added to your account!')

def save_user_details(user_credentials):                                # function to store user data in txt file
    with open('Accounts.txt', 'a') as file:
        file.write(user_credentials + '\n')

def register_user():                                                #function to register user duh
    while True:                                                     #can be optimised probably
        username = input("Please enter your username: ").lower()    #maybe later
        password = input("Please enter your password: ").lower()    #using if statement to check for potential
        user_id = randrange(10000,100000)                           #duplicates else saving them in txt file
        balance = 0
        if check_saved_users(username) is True:
            print('User already exists')
            break
        else:
            user_credentials = f"{username},{password},{user_id},{balance}"
            save_user_details(user_credentials)
            change_user_balance(username)
            choice = input("Do you want to add another user? (yes/no): ")
            if choice.lower() != "yes":
                break

def check_credentials(username, password):                 #function to check if user provided #valid login and password
    user_data = read_user_data()
    for user in user_data:
        if user[0] == username and user[1] == password:
            return True

def login(username, password):                                                 #login function for user to
    while True:               #get into his account
        if check_credentials(username, password) is True:
            print('login successful')
            return True
        else:
            print('Invalid credentials!!! Try again.')
            break


def check_user_balance(username):    #function to check balance of the logged user
    user_data = read_user_data()
    for user in user_data:
        if user[0] == username:
            print("You have", user[3],"$ in your account.")

def withdrawmoney(username, withmoney):  #function to withdraw money from the logged user
    user_data = read_user_data()
    for user in user_data:
        if user[0] == username:
            current_balance = int(user[3])
            if withmoney <= current_balance:
                new_balance = current_balance - withmoney
                user[3] = new_balance
                update_user_data(user_data)
                print(withmoney, '$ successfully withdrawed!')
                print('Your current balance is: ', new_balance,"$.")
            else:
                print("You don't have enough money.")
                print("Please check your balance and try again.")

def depositmoney(username, depomoney):  #function to deposit money from the logged user
    user_data = read_user_data()
    for user in user_data:
        if user[0] == username:
            current_balance = int(user[3])
            new_balance = current_balance + depomoney
            user[3] = new_balance
            update_user_data(user_data)
            print(depomoney, '$ successfully depostited!')
            print('Your current balance is: ', new_balance,"$.")

def transfer_money(username):                               #function to transfer money from logged user to
    user_data = read_user_data()                            #user2 after calling him
    print("This is the list of users than money can be transferred to:", [user[0] for user in user_data])
    user_for_transfer = input("Choose user to transfer money to: ").lower()
    money_to_transfer = int(input("How much money do you want to transfer: "))
    for user in user_data:
        if user[0] == username:
            current_balance = int(user[3])
            if current_balance >= money_to_transfer:
                new_balance = current_balance - money_to_transfer
                user[3] = new_balance
                update_user_data(user_data)

    for user2 in user_data:
        if user2[0] == user_for_transfer:
            current_balance = int(user2[3])
            new_balance = current_balance + money_to_transfer
            user2[3] = new_balance
            update_user_data(user_data)

# Welcome message
print("Welcome to the bank application made by Dolan!")
print("__________________________________________")

action_reg = input("Are you a registered user? (yes/no): ").lower()             #I should make this into a loop
if action_reg == "no":                                                          #with multiple options to choose
    register_user()

while True: #loop to log in user
    action_log = input("Do you want to login? (yes/no): ").lower()
    if action_log == "yes":
        while True: #second loop to get the credentials
            username = input("Please enter your username: ").lower()
            password = input("Please enter your password: ").lower()
            while login(username, password) is True: #third loop for logged user to make actions
                user_action = input("What do you want to do now? \
                (Check balance/Withdraw/Deposit/Transfer money/Log out): ").lower()
                if user_action == 'check balance':
                    check_user_balance(username)
                elif user_action == 'withdraw':
                    withmoney = int(input("How much money do you want to withdraw?: "))
                    withdrawmoney(username, withmoney)
                elif user_action == 'deposit':
                    try:
                        depomoney = int(input("How much money do you want to deposit? (max 500$ per transaction)"))
                        if depomoney <= 500:
                            depositmoney(username, depomoney)
                        else:
                            print("Please deposit no more than 500$ per one transaction")
                    except ValueError as e:
                        print(e)
                    finally:
                        continue
                elif user_action == 'transfer money':
                    transfer_money(username)
                elif user_action == 'log out':
                    print("User logged out...")
                    break
            break
    else:
        print("Program is shutting down, thank you for using it.")
        break