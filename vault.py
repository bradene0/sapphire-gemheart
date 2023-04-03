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

#Reads the passwords from file
with open('passwords.txt', 'r') as file:
    lines = file.readlines()

#Decrypts and prints passwords
for line in lines:
    username, website, encrypted_password = line.strip().split(',')
    password = fernet.decrypt(encrypted_password.encode()).decode()
    print(f"Username: {username}, Website: {website}, Password: {password}")
