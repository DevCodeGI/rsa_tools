import rsatool
from termcolor import colored
from getpass import getpass


## Main entry point    
while True:
    # Start to signature data
    answer = input("Do you want to signature from file (y/n)? ").lower()
    if answer == "y":
        file_name = input("Enter the file name? ")
        try:
            with open(file_name, "r") as f:
                message = f.read()
        except FileNotFoundError:
            print(colored("Error! No such file or directory.", "red"))  
            break     
        except IsADirectoryError:
            print(colored("Error! No such file or directory.", "red"))  
            break       
    else:
        message = input("Please enter the message to signature: ")
 
    password = getpass("Enter your password: ")
    signature = rsatool.signing_data(message, password)
    if signature is not None:
        print("-----BEGIN SIGNATURE-----\n"
                + signature
                + "\n-----END SIGNATURE-----")
        
    break