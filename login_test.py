import unittest
from login import User
from login import Credentials

class TestUser(unittest.TestCase):

    def test_create_new_user(self):

        line = "user|passwd"
        self.assertEqual(line,User.create_user(self))


class TestCredentials(unittest.TestCase):

    def test_add_credentials(self):

        cred = "facebook:123456"
        self.assertEqual(cred,Credentials.add_credentials(self))

    def test_display_credentials(self):
        creds = "facebook:123456"
        self.assertEqual(creds,Credentials.display_credentials(self))    




if __name__ == '__main__':
    unittest.main()
