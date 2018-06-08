class User:
    '''
    This is a class for the user
    '''
    def create_user(self):

        '''
        Function that allows one to create new users
        '''

        print("Enter the username that you would like to use \n")
        new_user  = input("Your Username: ")
        print("Enter a password")
        new_pass = getpass.getpass("Password: ")
        with open("created.txt", "a")as myfile:
            myfile.write("\n"+new_user + "|" + new_pass)
            return(new_user + "|" + new_pass)

user = User()


class Credentials:
    '''
    This is a class for the Credentials
    '''
