from user import User
import random
import string

class User_Credentials():
    """
    This will create an instance of an object
    """

    credentialsList = []

    def __init__(self, userAccount, username, password):

        """
        This will help define properties of our object
        """
        
        self.userAccount = userAccount
        self.username = username
        self.password = password

    
    #This will create new credentials
    def createNewCredentials(userAccount, username, password):
        """
        This will create new credentials structure for our accounts
        """
        
        newCredentials = User_Credentials(userAccount, username, password)
        return newCredentials

    #This will find user credentials
    @classmethod
    def findCredentials(cls, userAccount):

        """
        This will be used to select only userAccount credential
        """

        for credentials in cls.credentialsList:
            if credentials.userAccount == userAccount:
                return credentials
            return False

    #This will display user credentials           
    @classmethod
    def showCredentials(cls):

        """
        This function will be used to display an accounts credentials
        """        
        return cls.credentialsList


    #This will verify a user based on recorded username & passcode
    @classmethod
    def verifyUser(cls, username, password):

        """
        This function will be used for verification
        """
        for user in User.userList:
            if user.username == username and user.password == password:
                verifyUser = user.username
            return verifyUser

    def saveCredentials(self):

        """
        This method will be used to insert new credentials to the list
        """
        User_Credentials.credentialsList.append(self)

    def deleteCredentials(self):
        """
        This method will be used to delete an account and its credentials
        """
        User_Credentials.credentialsList.remove(self)

    def generatePasscode(length=8):

        """
        This method will be used to generate random password for users who choose free
        """
        password=string.hexdigits + string.ascii_lowercase + string.ascii_uppercase
        return "".join(random.choice(password)for i in range(length))
