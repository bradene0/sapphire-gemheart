import getpass
from cryptography.fernet import Fernet

#Generates a key to encrypt and decrypt the passwords
key = Fernet.generate_key()
fernet = Fernet(key)

#Prompt the user to enter their username, password, and website
username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")
website = input("Enter your website: ")

#Encrypts the password
encrypted_password = fernet.encrypt(password.encode())

#Stores the encrypted password along with username and website
with open('passwords.txt', 'a') as file:
    file.write(f"{username},{website},{encrypted_password.decode()}\n")

def get_passwords():
    passwords = {}
    with open('passwords.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            username, website, encrypted_password = line.strip().split(',')
            password = fernet.decrypt(encrypted_password.encode()).decode()
            passwords[website] = password
            return passwords
        
passwords = get_passwords()

for website, password in passwords.items():
    print(f"Website: {website}, Password: {password}")


        