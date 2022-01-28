import rsatool
from termcolor import colored


## Main entry point    
while True:
    # Start to encrypt data
    message = input("Please enter the message to encrypt: ")
    ciphertext = rsatool.encrypt(message)
    if ciphertext is not None:
        print("-----BEGIN ENCRYPTED-----\n"
                + ciphertext
                + "\n-----END ENCRYPED-----")
        
    break