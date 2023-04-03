import getpass
from cryptography.fernet import Fernet

#Generates a key to encrypt and decrypt the passwords
key = Fernet.generate_key()
fernet = Fernet(key)

