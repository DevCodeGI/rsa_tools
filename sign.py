import rsatool
from termcolor import colored
from getpass import getpass


## Main entry point    
while True:
    # Start to signature data
    message = input("Please enter the message: ")
    password = getpass("Enter your password: ")
    signature = rsatool.signing_data(message, password)
    if signature is not None:
        print("-----BEGIN SIGNATURE-----\n"
                + signature
                + "\n-----END SIGNATURE-----")
        
    break