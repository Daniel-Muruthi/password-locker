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

    def test_saveUser(self):
        self.newUser.saveUser()
        self.assertEqual(len(User.userList),1)

    def test_deleteUser(self):
        self.newUser.saveUser()
        defaultUser= User("Daniel-Muruthi", "12345678")
        defaultUser.saveUser()

        self.newUser.deleteUser()
        self.assertEqual(len(User.userList),1)

if __name__ == "__main__":
    unittest.main()