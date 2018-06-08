import unittest
from login import User
from login import Credentials

class TestUser(unittest.TestCase):

    def test_create_new_user(self):

        line = "user|passwd"
        self.assertEqual(line,User.create_user(self))


if __name__ == '__main__':
    unittest.main()
