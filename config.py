from getpass import getpass
from cryptography.fernet import Fernet

# Function for writing a key to encrypt and decrypt the admin password.
def write_key():
    key = Fernet.generate_key()
    with open("key2.key", "wb") as key_file:
        key_file.write(key)

# Function for reading the file that the key is stored and storing the key in a variable
def load_admin_key():
    file = open("key2.key", "rb")
    key = file.read()
    file.close()
    return key 

# Checking if there is a key already created, if not create a key 
with open("key2.key", "r") as check:
    checkfile = check.read()
    if checkfile == "":
        write_key()

key = load_admin_key()
fer = Fernet(key)

# decrypting the admin password (if the admin password is not set, does nothing)
def decrypt_admin_pwd():
    try:
        with open("admin.key", "r") as f:
            data = f.read()
            passw = fer.decrypt(data.encode()).decode()
            return passw
    except FileNotFoundError:
        pass

    
admin = decrypt_admin_pwd()

# If there is already an admin password set put the current admin password in a variable
try:
    with open("admin.key", "r") as ac:
        admincheck = ac.read()
# If there is no file called admin.key, pass this part (means that the admin password has not been set yet)
except FileNotFoundError:
    pass
# If the variable from "line 42" is not equal to an empty string (nothing), get input from user and compare the input to the decrypted admin password
try: 
    if admincheck != "":
        admin_pwd = str(getpass("Enter your current admin password to continue: "))
        if admin_pwd != admin:
            print("Acces denied.")
            exit()
except NameError:
    pass


# Main Interface to set password (and encrypt it)
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

