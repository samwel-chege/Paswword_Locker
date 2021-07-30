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