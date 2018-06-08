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

    def display_credentials(self):
        # '''
        # Functions that displays a users credentials
        # '''
        print("Please re-enter your username to confirm this action")
        user = input("username: ")
        f = open("login.txt", "r")
        for line in f.readlines():
            us, pw = line.strip().split("|")
            if (user in us):
                print("Username Confirmed")
                af = open(f"{user}", "r")
                for line in af.readlines():
                    yourResult = line.strip().split("\n")
                    for word in yourResult:
                        print(word)
                        return(word)
                return True
        print("wrong username")
        return False

    def generate_password(self):

        # '''
        # Function that generates new passwords for the user
        # '''

        import secrets
        import string
        print("Re-enter your username to confirm action")
        user = input("Username: ")
        f = open("login.txt", "r")
        for line in f.readlines():
            us, pw = line.strip().split("|")
            if (user in us):
                print("Username Confirmed")
                print("Enter the site which you will use the password")
                site = input("Site: ")
                print("Enter the length of password you want")
                length = int(input("Length: "))
                alphabet = string.ascii_letters + string.digits + string.punctuation
                password = ''.join(secrets.choice(alphabet) for i in range(length))
                with open(f"{user}", "a")as myfile:
                    myfile.write(site + ": "+ password + "\n")
                return True
        print("Wrong username")
        return False

    def copy_password(self):
        # '''
        # Function that copies passwords for a specific site to the clipboard
        # '''
        print("Please re-enter your username to confirm this action")
        user = input("username: ")
        f = open("login.txt", "r")
        for line in f.readlines():
            us, pw = line.strip().split("|")
            if (user in us):
                print("Username Confirmed")
                print("\n")
                af = open(f"{user}", "r")
                # for line in af.readlines():
                #     yourResult = line.strip().split("\n")
                #     for word in yourResult:
                #         print("Here are a list of credentials that can be copied")
                #         print(word)
                print("\n")
                print("Enter website name for password to be copied")
                site = input("Site: ")
                tf = open(f"{user}", "r")
                for line in tf.readlines():
                    sn, pw = line.strip().split(":")
                    if (site in sn) :
                        import pyperclip
                        pw = pw.strip()
                        pyperclip.copy(pw)
                        print(f"Password for {site} has been copied to the clipboard")
                        return(pw)
                return True
        print("wrong username")
        return False
