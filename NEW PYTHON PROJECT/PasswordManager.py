master_pwd = input("What is master password ? ")

def view():
    pass

def add():
    name = input('Account name: ')
    pwd = input("Password: ")
    
    with open("password.txt", "a") as f:
        f.write(name + "|" + pwd +"\n")

while True:
    mode = input("Would you like to add a new password or view the existing ones (View / Add ? or quit " )
    if mode ==  "q":
        break

    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid mode !")
        continue