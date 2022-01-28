import rsatool
from termcolor import colored
from getpass import getpass


## Main entry point    
while True:
    # Start to decrypt data
    ciphertext = input("Please enter the ciphertext: ")
    password = getpass("Enter your password: ")
    plaintext = rsatool.decrypt(ciphertext, password)
    if plaintext is not None:
        print("-----BEGIN PLAINTEXT-----\n"
                + plaintext
                + "\n-----END PLAINTEXT-----")
        
    break