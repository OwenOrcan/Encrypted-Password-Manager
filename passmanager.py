#PREPREQUISITES: 
#pip install cryptio
#pip install fernet
from getpass import getpass
from cryptography.fernet import Fernet

with open("key2.key", "r") as kc:
    keycheck = kc.read()

if keycheck == "":
    print("Please run the config file first to set your admin password")
    exit()

def load_admin_key():
    file = open("key2.key", "rb")
    key = file.read()
    file.close()
    return key

admin_key = load_admin_key()
admin_fer = Fernet(admin_key)

def decrypt_admin_key():
    with open("admin.key", "r") as f:
        data = f.read()
        passw = admin_fer.decrypt(data.encode()).decode()
        return passw

admin = decrypt_admin_key()

while True:
    adm_psw = str(getpass("What is the admin password: (Press q to exit) "))
    if adm_psw == "q":
        exit()
    if adm_psw != admin:
        print("Acces Denied")
        continue
    elif adm_psw == admin:
        break

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

with open("key_check.lock", "r") as readcheck:
    readed = readcheck.read()
if readed == "True":
    pass    
else:
    with open("key_check.lock", "w") as check:
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
    with open('passwords.lock', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            platform, user, passw = data.split("|")

            print("Platform:", platform, "User:", user, "Password:",
                fer.decrypt(passw.encode()).decode())

def add():  
    plf = input("Platform: ")
    name = input("Account name: ")
    pwd = input("Password: ")

    with open('passwords.lock', 'a') as f:
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
        print("Invalid input.")
        continue