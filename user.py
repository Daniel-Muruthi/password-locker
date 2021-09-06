class User:

    """
    This class will generate a new instance of user
    """

    userList = [] # Empty user list

    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def saveUser(self):

        """
        This will add a new user and their credentials to the userList dictionary
        """
        User.userList.append(self) 

    def deleteUser(self):

        """
        This will delete both an existing user and their credentials in the userList dictionary
        """
        User.userList.remove(self)
    
    @classmethod
    def user_accounts(cls):
        return cls.userList