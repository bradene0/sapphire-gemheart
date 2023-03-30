pwd = input("What is the main keyring password?")

def view():
    pass
def add():
    pass

while True:
    mode =input("Would you like to add a new password or view existing ones  (view, add), press q to quit? ").lower
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid Mode!")
        continue