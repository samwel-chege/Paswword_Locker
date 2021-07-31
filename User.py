class User:
    '''
    Class that generates new instances of users 
    '''
    user_list = []
    def __init__(self,first_name,last_name,sitename,passcode):

        self.first_name = first_name
        self.last_name = last_name
        self.sitename = sitename
        self.passcode = passcode

    def save_account(self):
        '''
        save_account method saves objects into user_list
        ''' 
        User.user_list.append(self) 

    def delete_account(self):
        '''
        delete_account method deletes a saved account from the user_list
        '''  
        User.user_list.remove(self) 

    @classmethod
    def find_by_sitename(cls,sitename):
        '''
        Method that takes in a  sitename and returns a contact that matches that sitename 

        Args:
            sitename: sitename to search.
        Returns:
               account of person that matches the sitename    
        ''' 

        for account in cls.user_list:
            if account.sitename == sitename:
                return account

    @classmethod
    def account_exist(cls,sitename):
        '''
        Method that checks if an account exists from the user_list
        Args:
             sitename:sitename to serach if it exists
        Returns:
             Boolean : True or false depending if the account exists       
        '''
        for account in cls.user_list == sitename:
            if account.sitename == sitename:
                return True

        return False

    @classmethod
    def display_account(cls):
        '''
        method that returns the user list
        ''' 
        return cls.user_list           

        
        
                     
