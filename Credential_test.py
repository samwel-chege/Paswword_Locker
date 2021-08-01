import unittest
from Credential import Credential

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user  class behaviours

    Args:
        unittest.TestCase: TestCase class that helps in creating test case 
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases 
        '''
        self.new_credential = Credential("Twitter","3421")

    def tearDown(self):
        '''
        tearDown  method that does clean up after each test case has run 
        '''
        Credential.credential_list = []
        

    def test_init(self):
        '''
        test_init case to test if the object id initialized properly 
        '''

        self.assertEqual(self.new_credential.sitename, "Twitter")
        self.assertEqual(self.new_credential.passcode, "3421")

    def test_save_credential(self):
        '''
        test_save_account test case to test if the user object is saved into the user list
        ''' 
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),1)  

    def test_save_multiple_credential(self):
        '''
        test save_multiple_credentials to check if we can save multiple credential objects to our credential_list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Twitter", "3421")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)

    def test_delete_credential(self):
        '''
        test delete_credential to test if we can remove a credential from our credential list 
        '''  
        self.new_credential.save_credential()
        test_credential = Credential("Twitter", "3421")
        test_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list),1)

    def test_credential_exists(self):
        '''
        test to check if we can return a Boolean if we cannot find the credential
        ''' 
        self.new_credential.save_credential()
        test_credential = Credential("Twitter", "3421")
        test_credential.save_credential()

        account_exists = Credential.credential_exist("Twitter")  

        self.assertTrue(account_exists)  

    def test_find_account_by_sitename(self):
        '''
        test to check if we can find a credential and display information using that sitename
        '''  
        self.new_credential.save_credential()
        test_credential = Credential("Twitter","3421")
        test_credential.save_credential()

        found_account = Credential.find_by_sitename("Twitter")  

        self.assertEqual(found_account.passcode,test_credential.passcode)

    def test_display_all_credential(self):
        '''
        method that returns a list of all credentials saved
        '''  

        self.assertEqual(Credential.display_credential(),Credential.credential_list)  

    

if __name__ == '__main__':
    unittest.main()                