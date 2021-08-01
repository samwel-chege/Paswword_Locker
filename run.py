#!/usr/bin/env python3
from User import User
from Credential import Credential
import string
import random
import pyperclip

def create_account(fname,lname,passcode):
    '''
    Function to create a new account 
    '''
    new_account  = User(fname,lname,passcode)
    return new_account

def save_account(account):
    '''
    Function to save accounts
    ''' 
    account.save_account() 

def create_credential(sitename,passcode):
    '''
    Function to create a new credential
    ''' 
    new_credential =Credential(sitename,passcode)
    return new_credential   

def save_credential(credential):
    '''
    Function to save credentials
    '''  
    credential.save_credential()  

def del_credential(credential):
    '''
    Function to delete an account
    ''' 
    credential.delete_credential()  

def find_credential(sitename):
    '''
    Function that finds an credential by sitename and returns the credential
    '''   
    return Credential.find_by_sitename(sitename)

def check_existing_credential(sitename):
    '''
    Function that checks if a credential exists with that sitename and return a Boolean
    '''
    return Credential.display_credential(sitename)  

def display_credential():
    '''
    Function that returns all the saved credentials
    '''
    return Credential.display_credential()      

def main():
    print("Hello Welcome to Password Locker.What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do? ")
    print('\n')

    while True:
        print(" Use these short codes: ca - create new account, si - sign in, ex -exit ") 

        short_code = input().lower()

        if short_code == 'ca':
            print("New account")
            print("_"*10)

            print("First name...")
            f_name = input()

            print("Last name...")
            l_name = input()

            print("passcode...")
            passcode = input()

            save_account(create_account(f_name,l_name,passcode))
            print('\n')
            print(f"New account {f_name} {l_name} created")
            print('\n')

        elif short_code == 'si':
            print("Enter your first name")
            default_f_name = input()

            print("Enter your passcode")
            default_passcode = input()

            while default_f_name != f_name or default_passcode != passcode:
                print("Wrong first name or passcode.")
                print("Enter your first name")
                default_f_name = input()

                print("Enter passcode")
                default_passcode = input()
                print('\n')

            else:
                print("Sign in was succesful")
                print('\n')

            while True:    
                print("Use these short code to proceed: sc - save credentials, dc- display credentials, fc- find existing credentials, q-quit")
                
                short_code = input().lower()

                if short_code == 'sc':
                    print("New credentials")
                    print("_"*10)
                    
                    print("Enter the site name")
                    sitename = input()

                    print("Proceed with: gc to generate passcode; cc to create passcode")
                    gpasscode = input()
                    if gpasscode == 'gc':
                        passcode =  ''.join(random.choice(string.printable) for i in range(14))
                        print("Random password is:", passcode)

                    else:
                        print("Enter the site's passcode") 
                        passcode = input()   


                    save_credential(create_credential(sitename,passcode))
                    print('\n')
                    print("New credentials were saved succesfully")
                    print('\n')

                elif short_code == 'dc':

                    if find_credential(sitename):
                        print("Here is a list of all the credentials")
                        print('\n')

                        for credential in display_credential():
                            print(f" Sitename:{credential.sitename} \n Passcode:{credential.passcode}")

                            print('\n')
                    else:
                         print('\n')
                         print("Credentials  does not exist") 
                         print('\n')           
                    

                elif short_code == 'fc':

                    print("Enter the sitename for the site you are looking for you ")

                    search_credential = input()
                    if check_existing_credential(search_credential):
                        search_passcode = find_credential(search_credential)
                        
                        print(f"Sitename...{search_passcode.sitename} ")
                        print(f"passcode... {search_passcode.passcode} ")

                    else:
                        print("That credentials does not exist") 

                elif short_code == "q":
                        print("Thanks for using the application")
                        break
                else:
                    print("I didn't really get that please use the short codes") 

        elif short_code == "ex":
            print("Have a great day!") 
            break
        else:
            print("Enter a correct shortcode")            

if __name__ == '__main__':

    main()                     






