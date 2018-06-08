class User:
    '''
    This is a class for the user
    '''
    def create_user(self):

        # '''
        # Function that allows one to create new users
        # '''

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
    def add_credentials(self):

        # '''
        # Function that allows the user to add credentials
        # '''

        print("Please re-enter your username to confirm this action")
        user = input("username: ")
        f = open("login.txt", "r")
        for line in f.readlines():
            us, pw = line.strip().split("|")
            if (user in us):
                print("Username Confirmed")
                print("\n")
                print("Enter credentials")
                site_name = input("Enter site: ")
                password = input("existing password: ")
                with open(f"{user}", "a")as myfile:
                    myfile.write(site_name + ":" + password + "\n")
                    return(site_name + ":" + password)
                return True
        print("Wrong username")
        return False
