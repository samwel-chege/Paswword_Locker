import unittest
from User import User

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
        self.new_account = User("Sammie", "Sam", "3421")

    def tearDown(self):
        '''
        tearDown  method that does clean up after each test case has run 
        '''
        User.user_list = []
        

    def test_init(self):
        '''
        test_init case to test if the object id initialized properly 
        '''

        self.assertEqual(self.new_account.first_name, "Sammie")
        self.assertEqual(self.new_account.last_name, "Sam")
        self.assertEqual(self.new_account.passcode, "3421")

    def test_save_account(self):
        '''
        test_save_account test case to test if the user object is saved into the user list
        ''' 
        self.new_account.save_account()
        self.assertEqual(len(User.user_list),1)  

    def test_save_multiple_account(self):
        '''
        test save_multiple_accounts to check if we can save multiple account objects to our user_list
        '''
        self.new_account.save_account()
        test_account = User("Test","user", "3421")
        test_account.save_account()
        self.assertEqual(len(User.user_list),2)

    def test_delete_account(self):
        '''
        test delete_account to test if we can remove an account from our user list 
        '''  
        self.new_account.save_account()
        test_account = User("Test", "user", "3421")
        test_account.save_account()

        self.new_account.delete_account()
        self.assertEqual(len(User.user_list),1) 



if __name__ == '__main__':
    unittest.main()        
