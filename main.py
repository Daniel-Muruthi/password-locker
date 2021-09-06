# from user import User


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
                print("Enter a Username")
                new_username = input()
                print("Enter a password")
                new_password = input()
                print(f"{new_username} confirm your password")
                confirm_password = input()

                if (confirm_password != new_password):
                    print("Password do not match. Please try again")
                    print("Enter a password")
                    new_password = input()
                    print(f"{new_username} confirm your password")
                    confirm_password = input()
                else:
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
                break

            else:

                print("Enter valid code to continue")



        else:
            print("Thank you for visiting us. Thanks!")


if __name__=="__main__":
    main()
        