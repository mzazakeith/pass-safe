import unittest
from login import User
from login import Credentials

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def test_create_new_user(self):

        '''
        test_create_new_user test case to test if a user is being created
        '''

        line = "user|passwd"
        self.assertEqual(line,User.create_user(self))


class TestCredentials(unittest.TestCase):
        '''
        Test class that defines test cases for the credentials class behaviours.

        Args:
            unittest.TestCase: TestCase class that helps in creating test cases
        '''

    def test_add_credentials(self):

        '''
        test_add_credentials test case to test if credentials are being added
        '''

        cred = "facebook:123456"
        self.assertEqual(cred,Credentials.add_credentials(self))

    def test_display_credentials(self):

        '''
        test_display_credentials test case to test if credentials are being diaplayed
        '''

        creds = "facebook:123456"
        self.assertEqual(creds,Credentials.display_credentials(self))

    def test_copy_password(self):

        '''
        test_copy_password test case to test if a password can be copied
        '''

         copied = "123456"
         import pyperclip
         self.assertEqual(copied,Credentials.copy_password(self))




if __name__ == '__main__':
    unittest.main()
