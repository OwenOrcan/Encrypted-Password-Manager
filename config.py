from getpass import getpass
from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key2.key", "wb") as key_file:
        key_file.write(key)

def load_admin_key():
    file = open("key2.key", "rb")
    key = file.read()
    file.close()
    return key 

with open("key2.key", "r") as check:
    checkfile = check.read()
    if checkfile == "":
        write_key()

key = load_admin_key()
fer = Fernet(key)


def decrypt_admin_key():
    try:
        with open("admin.key", "r") as f:
            data = f.read()
            passw = fer.decrypt(data.encode()).decode()
            return passw
    except FileNotFoundError:
        pass

    
admin = decrypt_admin_key()

try:
    with open("admin.key", "r") as ac:
        admincheck = ac.read()
except FileNotFoundError:
    pass
try:
    if admincheck != "":
        admin_pwd = str(getpass("Enter your current admin password to continue: "))
        if admin_pwd != admin:
            print("Acces denied.")
            exit()
except NameError:
    pass
    
while True:
    admin_passw = getpass("What is your new admin password? ")
    if len(admin_passw) < 2:
        input("Admin password should be atleast 2 characters long...")
        continue
    else:
        break
with open("admin.key", "w") as f:
    f.write(fer.encrypt(admin_passw.encode()).decode())
    f.close()
    print("Password Set!")

