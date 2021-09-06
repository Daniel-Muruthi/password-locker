import unittest # importing the unittest module
from user import User

class testUsers(unittest.TestCase):
    def setUp(self):
        """
        This method runs before any test
        """
        self.newUser = User("daniel", "12345678")
    def tearDown(self):
        User.userList = []

    def test_init(self):
        """
        test case to check if object or class is instanciated properly 
        """
        self.assertEqual(self.newUser.username, 'daniel')
        self.assertEqual(self.newUser.password, '12345678')


if __name__ == "__main__":
    unittest.main()