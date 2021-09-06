from user import User
import random
import string

class User_Credentials:
    """
    This will create an instance of an object
    """

    credentialsList = []

    def __init__(self, userAccount, username, passcode):
        
        self.userAccount = userAccount
        self.username = username
        self.passcode = passcode


    #This will find user credentials
    @classmethod
    def findCredentials(cls, account):
        for credentials in cls.credentialsList:
            if credentials.account == account:
                return credentials

    #This will display user credentials           
    @classmethod
    def showCredentials(cls):
        return cls.credentialsList


    #This will verify a user based on recorded username & passcode
    @classmethod
    def verifyUser(cls, username, passcode):
        for user in User.userList:
            if user.username == username and user.passcode == passcode:
                verifyUser = user.username
            return verifyUser

    def saveCredentials(self):
        User_Credentials.credentialsList.append(self)

    def deleteCredentials(self):
        User_Credentials.credentialsList.remove(self)

    def generatePasscode(length=8):
        passcode=string.hexdigits + string.ascii_lowercase + string.ascii_uppercase
        return "".join(random.choice(passcode)for i in range(length))
