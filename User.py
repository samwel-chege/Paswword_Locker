class User:
    '''
    Class that generates new instances of users 
    '''
    user_list = []
    def __init__(self,first_name,last_name,passcode):

        self.first_name = first_name
        self.last_name = last_name
        self.passcode = passcode

    def save_account(self):
        '''
        save_account method saves objects into user_list
        ''' 
        User.user_list.append(self) 

   

        
        
                     
