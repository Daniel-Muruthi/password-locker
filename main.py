from user import User
from credentials import User_Credentials
import test

def showCredentials():

    return User_Credentials.showCredentials()



def main():

    print("Hello there and welcome to Password Locker!")

    while True:
        print("Do you wish to proceed? (answer with 'yes' or 'no')")
        proceed_answer=input()
        if (proceed_answer=='yes'):
            print("Kindly use these short codes to access out services : 'cua' - To create new password locker account, 'lga' - To login into your password locker account, 'dua' - To display user accounts or 'ex' - To exit your account")

            short_code = input().lower()
            #Taking service input codes 
            if (short_code) == 'cua':
                print("Enter Account Name")
                new_account = input().lower()
                print("Enter a Username")
                new_username = input()
                print("To input your own password reply with 'self'. To use a randomly generated password reply with 'free'")
                new_password = input().lower()
                if (new_password == 'self'):
                    print("Enter your password")
                    password=input()
                    print(f"{new_username} confirm your password")
                    confirm_password = input()
                    if (confirm_password != password):
                        print("Password do not match. Please try again")
                        print("Enter a password")
                        password = input()
                        print(f"{new_username} confirm your password")
                        confirm_password = input()
                    else:
                        print(f" You have set '{password}' as your password")
                        print(f"Welcome {new_username} to your new account. Your account has been created successflully")
                        print("Log into your account")
                        print("Enter Username")
                        new_login_username=input()
                        print("Enter you password")
                        new_login_password= input() 
                        while (new_login_username != new_username or new_login_password != new_password):
                            print("Your login credentials do not match any account...try again") 
                            print("Enter Username")
                            new_login_username=input()
                            print("Enter you password")
                            new_login_password= input() 


                        else:
                            print(f"Greetings {new_username}! Welcome to your account")


                elif(new_password == 'free'):
                    password = User_Credentials.generatePasscode()
                    print(f"Your password has been set to {password}")

                User_Credentials.saveCredentials(User_Credentials.createNewCredentials( new_account, new_username, password))

                print(f"{new_username} your account {new_account} is Active!")

                print("Do you wish to view your credentials? (Answer with 'yes' or 'no')")
                response=input().lower()
                if response == 'yes':
                    if showCredentials():

                        for credentials in showCredentials():
                            print(f"Username : {credentials.username}")
                            print(f"Account : {credentials.userAccount}")
                            print(f"Password : {credentials.password}")
                    else :
                        print("There are no credentials associated with this username")

                elif response == 'no':
                    print("Okay")

                else:
                    print("Error! your input is not recognized")
                    break
                    


            elif short_code == 'dua':
                print(f"Hello. Here is a list of your credentials")
                
                if User_Credentials.showCredentials():

                    for credentials in User_Credentials.showCredentials():
                        print(credentials)
                else :
                    print("There are no credentials associated with this username")


            
            elif short_code == 'lga':
                print("welcome to the login page")
                print("Please enter your name")
                saved_username = input()
                print("Please enter your password")
                saved_password = input()

                while (saved_username !="Daniel-Muruthi" or saved_password != "12345678"):
                    print("Wrong username or password! Please enter correct credentials")
                    print("Please enter your name")
                    saved_username = input()
                    print("Please enter your password")
                    saved_password = input()

            elif short_code == 'ex':
                print(f"Goodble {new_username}")
                break

            else:

                print("Enter valid code to continue")



        else:
            return print("Thank you for visiting us. Thanks!")
            


if __name__=="__main__":
    main()
        