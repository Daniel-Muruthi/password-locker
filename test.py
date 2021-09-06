from credentials import User_Credentials
import unittest # importing the unittest module
from user import User
from credentials import User_Credentials

class testUsers(unittest.TestCase):
    def setUp(self):
        """
        This method runs before any test
        """
        self.credentialsList = User_Credentials("facebook", "daniel", "12345678")
    def tearDown(self):

        '''
        tearDown method that does clean up after each test case has run.
        '''
        User_Credentials.credentialsList = []

    def test_init(self):
        """
        test case to check if object or class is instanciated properly 
        """
        self.assertEqual(self.credentialsList.userAccount, 'facebook')
        self.assertEqual(self.credentialsList.username, 'daniel')
        self.assertEqual(self.credentialsList.password, '12345678')

    def test_saveUser(self):

        """
        test case to check if objects are saved properly 
        """ 
        self.credentialsList.saveCredentials()
        self.assertEqual(len(User_Credentials.credentialsList),1)

    def test_deleteUser(self):

        """
        test case to check if credentials are deleted properly
        """
        self.credentialsList.saveCredentials()
        test_multi_credentials = User_Credentials("twitter", "el_asad_the_don ", " 1234")
        test_multi_credentials.saveCredentials()
        self.credentialsList.deleteCredentials()
        self.assertEqual(len(User.userList),0)

if __name__ == "__main__":
    unittest.main()