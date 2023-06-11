master_pwd = input("Master password: ")

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(f"[Acc name: {name}], [password: {pwd}] \n")

def view():
    pass

while True:
    mode = input("To add a new password 'add'"
                 "and to view existing ones 'view'"
                 "to quit 'q': ").lower()
    if mode == 'q':
        break
    if mode == 'add':
        add()
    elif mode == 'view':
        view()
    else:
        print("invalid mode")
