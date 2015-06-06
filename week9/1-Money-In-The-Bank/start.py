import sql_manager
import getpass
from datetime import datetime
from Client import Client

# need to make usernames unique
# brute force while accessing the database
# need to check mail validation and uniqueness
# fix the creation of the database with settings.py and shit like that
# for friday learn alchemy ORM !!!!!!!!!!!!!!!!!!!!!!!!


def main_menu():
    print("Welcome to our bank service. You are not logged in. \nPlease register or login")
    while True:
        command = input("$$$>")

        if command == 'register':
            username = input("Enter your username: ")
            password = getpass.getpass(prompt="Enter your password: ")
            email = input("Enter your email:")
            if sql_manager.register(username, password, email):
                print("Registration successfull")
            else:
                print("Registration unsuccessfull.Password is too weak.")

        elif command == 'login':
            username = input("Enter your username: ")
            password = getpass.getpass(prompt="Enter your password:")

            logged_user = sql_manager.login(username, password)

            if isinstance(logged_user, Client):
                logged_menu(logged_user)
            else:
                print(sql_manager.login(username, password))
        elif command == 'help':
            print("login - for logging in!")
            print("register - for creating new account!")
            print("exit - for closing program!")

        elif command == 'exit':
            break

        elif 'send-reset-password' in command:
            username = command[len('send-reset-password '):]
            sql_manager.send_reset_password(username)

        elif 'reset-password' in command:
            username = command[len('reset-password '):]
            code = input("Enter your code:")
            if sql_manager.check_code_to_reset(code, username):
                new_pass = getpass.getpass(prompt="Enter your new password:")
                sql_manager.reset_password(new_pass, username)
            else:
                print("Invalid code to reset!")
        else:
            print("Not a valid command")


def logged_menu(logged_user):
    print("Welcome you are logged in as: " + logged_user.get_username())
    while True:
        command = input("Logged>>")

        if command == 'info':
            print("You are: " + logged_user.get_username())
            print("Your id is: " + str(logged_user.get_id()))
            balance = sql_manager.balance(logged_user.get_username())
            print("Your balance is:{}$".format(balance))

        elif command == 'changepass':
            new_pass = input("Enter your new password: ")
            sql_manager.change_pass(new_pass, logged_user)

        elif command == 'change-message':
            new_message = input("Enter your new message: ")
            sql_manager.change_message(new_message, logged_user)

        elif command == 'show-message':
            print(logged_user.get_message())

        elif command == 'help':
            print("info - for showing account info")
            print("changepass - for changing passowrd")
            print("change-message - for changing users message")
            print("show-message - for showing users message")
            print("show-balance - for showing balance")
            print("get-tan - sends TAN code to email")
            print("deposit - for depositing money")

        elif command == 'show-balance':
            balance = sql_manager.balance(logged_user.get_username())
            print("Your balance is: {}".format(balance))

        elif command == 'get-tan':
            password = getpass.getpass(prompt="Enter your password:")
            user = sql_manager.login(logged_user.get_username(), password)
            if user:
                sql_manager.send_tan_code(logged_user.get_username())
            else:
                print("Wrong password!")

        elif command == 'deposit':
            amount = input("Enter amount:")
            amount = int(amount.replace(' ', '').strip())
            code = input("Enter TAN code:")
            if sql_manager.check_tan_code(code, logged_user.get_username()):
                sql_manager.deposit(amount, logged_user.get_username())
                print("Transaction successfull!")
                print("{} were deposited in your acount".format(amount))
            else:
                print("Wrong TAN code!")

        elif command == 'withdraw':
            amount = input("Enter amount:")
            amount = int(amount.replace(' ', '').strip())
            code = input("Enter TAN code:")
            if sql_manager.check_tan_code(code, logged_user.get_username()):
                sql_manager.withdraw(amount, logged_user.get_username())
                print("Transaction successfull!")
                print("{} were withdrawn in your acount".format(amount))
            else:
                print("Wrong TAN code!")

        elif command == 'exit':
            break

        else:
            print("Not a valid command")
# need to delete TAN code after being used
# and also delete code_to_reset after being used


def main():
    sql_manager.create_clients_table()
    main_menu()

if __name__ == '__main__':
    main()
