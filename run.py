#!/usr/bin/env python3
from User import User

def create_account(fname,lname,sitename,passcode):
    '''
    Function to create a new account 
    '''
    new_account  = User(fname,lname,sitename,passcode)
    return new_account

def save_account(account):
    '''
    Function to save accounts
    ''' 
    account.save_account() 

def del_account(account):
    '''
    Function to delete an account
    ''' 
    account.delete_account()  

def find_account(sitename):
    '''
    Function that finds an account by sitename and returns the account
    '''   
    return User.find_by_sitename(sitename)

def check_existing_account(sitename):
    '''
    Function that checks if a contact exists with that number and return a Boolean
    '''    

def main():
    print("Hello Welcome to Password Locker.What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do? ")
    print('/n')

    while True:
        print(" Use these short codes: ca - create new account, fa - find an account, ex -exit ") 

        short_code = input().lower()

        if short_code == 'ca':
            print("New account")
            print("_"*10)

            print("First name...")
            f_name = input()

            print("Last name...")
            l_name = input()

            print("sitename...")
            sitename = input()

            print("passcode...")
            passcode = input()

            save_account(create_account(f_name,l_name,sitename,passcode))
            print('/n')
            print(f"New account {f_name} {l_name} created")
            print('/n')

        elif short_code == 'fa':

            print("Enter the sitename for the site you are looking for you ")

            search_sitename = input()
            if check_existing_account(search_account):
                search_account = find_account(search_sitename)
                print(f" {search_account.first_name} {search_account.last_name} ")
                print('_' * 20)

                print(f"Sitename...{search_account.sitename} ")
                print(f"passcode... {search_account.passcode} ")

            else:
                print("That account does not exist") 

        elif short_code == "ex":
            print("Have a goodday!")
            break
        else:
            print("I didn't really get that please use the short codes")  

if __name__ == '__main__':

    main()                     






