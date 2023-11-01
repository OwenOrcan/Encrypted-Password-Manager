from getpass import getpass

while True:
    admin_passw = getpass("What is your new admin password? ")
    if len(admin_passw) < 2:
        input("Admin password should be atleast 2 characters long...")
        continue
    else:
        break
with open("admin.py", "w") as f:
    f.write(f"ADMIN_PWD = '{admin_passw}'")
    f.close()
    print("Password Set!")