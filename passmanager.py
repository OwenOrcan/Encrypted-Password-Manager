from getpass import getpass
from cryptography.fernet import Fernet

############################# Admin Password Part ##########################

#check the file for encryption key for admin password
with open("key2.key", "r") as kc:
    keycheck = kc.read()
# if there is no key in the file exit the program
if keycheck == "":
    print("Please run the config file first to set your admin password")
    exit()
# put the admin encryption key inside a variable
def load_admin_key():
    file = open("key2.key", "rb")
    key = file.read()
    file.close()
    return key


admin_key = load_admin_key()
admin_fer = Fernet(admin_key)

# decrypt the admin password using the key from the load_admin_key function
def decrypt_admin_key():
    with open("admin.key", "r") as f:
        data = f.read()
        passw = admin_fer.decrypt(data.encode()).decode()
        return passw

# put the decrpted admin password inside a variable to compare it to the input
admin = decrypt_admin_key()

# compare the input to the  the admin password
while True:
    adm_psw = str(getpass("What is the admin password: (Press q to exit) "))
    if adm_psw == "q":
        exit()
    if adm_psw != admin:
        print("Acces Denied")
        continue
    elif adm_psw == admin:
        break

############################# Password Manager Part ##############################
# Function to make a key to encrypt and decrypt the passwords and storing the key inside key.key
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


# Checking if a key has already been set, if not create a key.
with open("key_check.lock", "r") as readcheck:
    readed = readcheck.read()
if readed == "True":
    pass    
else:
    with open("key_check.lock", "w") as check:
        write_key()
        check.write("True")

# Function to get the key from key.key and store it in a variable.
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key 


key = load_key()
fer = Fernet(key)
 
# Function for viewing the saved Accounts and Passwords.
def view():
    with open('passwords.lock', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            platform, user, passw = data.split("|")

            # Printing the decrpyted data.
            print("Platform:", platform, "User:", user, "Password:",
                fer.decrypt(passw.encode()).decode())

# Function for adding new account data.
def add():  
    plf = input("Platform: ")
    name = input("Account name: ")
    pwd = input("Password: ")

    # encrypting the inputted password and storing it inside passwords.lock
    with open('passwords.lock', 'a') as f:
        f.write(plf + "|" + name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

# Main Interface
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