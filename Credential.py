import pyperclip
class Credential:
    '''
    class that creates new instances of credentials 
    '''
    credential_list = []

    def __init__(self,sitename,passcode):

        self.sitename = sitename
        self.passcode = passcode

    def save_credential(self):
        '''
        method that saves credential objects into credential_list
        '''  
        Credential.credential_list.append(self)

    def delete_credential(self):
        '''
        method deletes credential saved on the credential list
        ''' 
        Credential.credential_list.remove(self) 

    @classmethod
    def find_by_sitename(cls,sitename):
        '''
        Method that takes in a sitename and returns  the sites's credentials.

        Args:
            sitename: site to search for 
        Returns:
            Credentails that matches that sitename.  
        '''
        for credential in cls.credential_list:
            if credential.sitename == sitename:
                return credential

    @classmethod
    def credential_exist(cls,sitename):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
            sitename: site to search for  
        Returns: 
            Boolean: True or false depending if the credential exists         

        ''' 
        for credential in cls.credential_list:
            if credential.sitename == sitename:
               return True

        return False

    @classmethod
    def display_credential(cls):
        '''
        method that returns the credential list 
        '''                   
        return cls.credential_list 

    @classmethod
    def copy_passcode(cls,sitename):
        passcode_found = Credential.find_by_sitename(sitename)
        pyperclip.copy(passcode_found.passcode)    
                
        