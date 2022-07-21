import sys
import threading
import os

class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def run(self):
        try:
            files = open(f'{self.username}', 'r')
            for x in files:
                if self.username in x and self.password in x:
                    user_thread = threading.Thread(target=self.user, args=())
                    user_thread.start()

        except KeyboardInterrupt:
            print('Login is interrupted!')
            sys.exit()

    def admin(self):
        print("This is admin pass!")
        sys.exit(0)
       
    def user(self):
        print("This is user pass!")
        sys.exit(0)


def check_account(username, password):

    if username == 'admin' and password == 'admin':
        login = Login(username, password)
        login.admin()
    elif os.path.exists(f'{username}.txt'):
        login = Login(username, password)
        login.run()
    else:
        print("Your account not found! Please register first!")
        register = Register(True)
        register.run()


class Register: 

    def __init__(self, register=False):
        self.register = register
        self.account = []

    def run(self):
        if self.register:
            username = input("Username  : ")
            password = input("Password  : ")
            
            self.account = [username, password]

            files = open(f'{username}.txt', "a")
            for x in range(len(self.account)):
                files.write(self.account[x] + "\n")
            
            check_account(username, password)


if __name__ == '__main__':
    username = input("Username : ")
    password = input("Password : " )

    try:
        while True:
            check_account(username, password)

    except KeyboardInterrupt:
        print("Exit!!")
        sys.exit()
