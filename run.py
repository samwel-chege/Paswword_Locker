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