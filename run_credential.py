#!/usr/bin/env python3.6
from credential import Credentials


def create_credential(Username,password):
        '''
        Function to create a new credential
        '''
        new_credential = Credentials(Username,password)
        return new_credential

def save_credential(credential):
        '''
        Function to save credential
        '''
        credential.save_credential()

def del_credential(credential):
        '''
        Function to delete a credential
        '''
        credential.delete_credential()

def find_credential(Username):
        '''
        Function that finds a credential by Username and returns the credential
        '''
        return Credentials.find_by_Username(Username)

def check_existing_credential(Username):
        '''
        Function that check if a credential exists with that Username and return a Boolean
        '''
        return Credentials.credential_exist(Username)
        

def display_credential():
        
        '''
        Username = input()
        Function that returns all the saved credential
        '''
        return Credentials.display_credential()

        #Main function for Credentials
def main():
        print("Login----------")
        print("Hello Welcome to your credential list. What is your name?")
        Username = input()

        print("Hello Welcome to your credential list. What is your password?")
        password = input()

        print(f"Hello {Username}. what would you like to do?")
        print('\n')


        while True:
            print("Use these short codes : cc - create a new credential, dc - display credential, fc -find a credential, del - delete credential, ex -exit the credential list ")

            short_code = input().lower()

            if short_code == 'cc':
                print("New Credentials")
                print("-"*10)

                print("Username ...")
                Username = input()

                print("password ...")
                password = input()

                save_credential(create_credential(Username,password)) # create and save new credential.
                print ('\n')
                print(f"New Credentials {Username} {password} created")
                print ('\n')

            elif short_code == 'dc':

                if display_credential():
                    print("Here is a list of all your credential")
                    print('\n')

                for credential in display_credential():
                        print(f"{credential.Username} .....{credential.password}")
                        print('\n')

                else:
                        print('\n')
                        print("You dont seem to have any credential saved yet")
                        print('\n')

            elif short_code == 'fc':

                print("Enter the Username you want to search for")

                search_Username = input()
                if check_existing_credential(search_Username):
                    search_credential = find_credential(search_Username)
                    print(f"{search_credential.Username} {search_credential.password}")
                    print('-' * 20)


                    print(f"Username.......{search_credential.Username}")
                    print(f"password.......{search_credential.password}")
                else:
                    print("That credential does not exist")

            elif short_code == "ex":
                print("Bye .......")
                break
            else:
                print("I really didn't get that. Please use the short codes")


            

            #delete user information

            # elif short_code == 'del':

            #     print("Delete password of credential list")

            #     if delete_credential():
            #         print("Here is a list of all your credential")
            #         print('\n')

            # # credential_list = ["Username,password"]
            # # del credential_list["password"]

            # print ("List credential after deleting are : ",end="")

            # for credential_list in delete_credential():
            #     print(f"{credential.password}")

            #     print("\n")

            

if __name__ == '__main__':

    main()


