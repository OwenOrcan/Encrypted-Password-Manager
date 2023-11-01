#pip install cryptio
#pip install fernet
from cryptography.fernet import Fernet
from admin import ADMIN_PWD
from getpass import getpass


while True:
    adm_psw = str(getpass("What is the admin password: (Press q to exit) "))
    if adm_psw == "q":
        break
    if adm_psw != ADMIN_PWD:
        print("Acces Denied")
        continue
    elif adm_psw == ADMIN_PWD:
        break

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

with open("key_check.txt", "r") as readcheck:
    readed = readcheck.read()
if readed == "True":
    pass    
else:
    with open("key_check.txt", "w") as check:
        write_key()
        check.write("True")

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key 


key = load_key()
fer = Fernet(key)
 

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            platform, user, passw = data.split("|")

            print("Platform:", platform, "User:", user, "Password",
                fer.decrypt(passw.encode()).decode())

def add():  
    plf = input("Platform: ")
    name = input("Account name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(plf + "|" + name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input("Would you like to add a password or view existing ones (view,add)? press q to quit: ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
        print("Account saved!")
    else:
        print("Invalid mode.")
        continue