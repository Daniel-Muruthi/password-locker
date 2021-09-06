from user import User
import random
import string

class User_Credentials():
    """
    This will create an instance of an object
    """

    credentialsList = []

    def __init__(self, userAccount, username, password):
        
        self.userAccount = userAccount
        self.username = username
        self.password = password

    
    #This will create new credentials
    def createNewCredentials(userAccount, username, password):
        newCredentials = User_Credentials(userAccount, username, password)
        return newCredentials

    #This will find user credentials
    @classmethod
    def findCredentials(cls, username):
        for credentials in cls.credentialsList:
            if credentials.username == username:
                return credentials

    #This will display user credentials           
    @classmethod
    def showCredentials(cls):
        return cls.credentialsList


    #This will verify a user based on recorded username & passcode
    @classmethod
    def verifyUser(cls, username, password):
        for user in User.userList:
            if user.username == username and user.password == password:
                verifyUser = user.username
            return verifyUser

    def saveCredentials(self):
        User_Credentials.credentialsList.append(self)

    def deleteCredentials(self):
        User_Credentials.credentialsList.remove(self)

    def generatePasscode(length=8):
        password=string.hexdigits + string.ascii_lowercase + string.ascii_uppercase
        return "".join(random.choice(password)for i in range(length))
