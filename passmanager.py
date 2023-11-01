from cryptography.fernet import Fernet

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key 



key = load_key()
fer = Fernet(key)

# DELETE THE QUOTES AND RUN THE PROGRAM ONCE THEN PUT THE QOUTES BACK"
''' 
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key) 
        
write_key()''' 

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            platform, user, passw= data.split("|")
            

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
