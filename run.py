#!/usr/bin/env python3.6
from user import User

def create_user(user_account,Username,password,email):
    '''
    Function to create a new user
    '''
    new_user = User(user_account,Username,password,email)
    return new_user

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def find_user(email):
    '''
    Function that finds a user by email and returns the user
    '''
    return User.find_by_email(email)

def check_existing_user(email):
    '''
    Function that check if a user exists with that email and return a Boolean
    '''
    return User.user_exist(email)

def display_user():
    '''
    Function that returns all the saved user
    '''
    return User.display_user()

#Main function for User
def main():
    print("Login----------")
    print("Username")
    Username = input()

    print("Password")
    password = input()

    print(f"Hello {Username}. what would you like to do?")
    print('\n')

    while True:
            print("Use these short codes : cc - create a new user, dc - display user, fc -find a user, ex -exit the user list ")

            short_code = input().lower()

            if short_code == 'cc':
                print("New User")
                print("-"*10)

                print ("user_account ....")
                user_account = input()

                print ("Username ....")
                Username = input()

                print("password ...")
                password = input()

                print("email ...")
                email = input()

                save_user(create_user(user_account,Username,password,email)) # create and save new user.
                print ('\n')
                print(f"New User {Username} {password} created")
                print ('\n')

            elif short_code == 'dc':

                if display_user():
                    print("Here is a list of all your user")
                    print('\n')

                    for user in display_user():
                        print(f"{user.user_account} {user.Username} .....{user.email}")

                        print('\n')
                    else:
                        print('\n')
                        print("You dont seem to have any user saved yet")
                        print('\n')

            elif short_code == 'fc':

                print("Enter the email you want to search for")

                search_email = input()
                if check_existing_user(search_email):
                    search_user = find_user(search_email)
                    print(f"{search_user.user_account} {search_user.Username} {search_user.email}")
                    print('-' * 20)


                    print(f"user_account.......{search_user.user_account}")
                    print(f"Username.......{search_user.Username}")
                    print(f"email.......{search_user.email}")
                else:
                    print("That user does not exist")


            elif short_code == "ex":
                print("Bye .......")
                break
            else:
                print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':

    main()


