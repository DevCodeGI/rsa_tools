from rsatool import rsatool
from termcolor import colored

    
## Main entry point    
while True:
    # Create object
    rsatool = rsatool()
    
    # Start to validation signature
    answer = input("Do you want to validate the signature from file (y/n)? ").lower()
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
        message = input("Please enter the message to vaidate the signature: ")
        
    
    # Input Signature
    print()
    answer = input("Do you want to read the signature from file (y/n)? ").lower()
    if answer == "y":
        file_name = input("Enter the file name? ")
        try:
            with open(file_name, "r") as f:
                signature = f.read()
        except FileNotFoundError:
            print(colored("Error! No such file or directory.", "red"))  
            break     
        except IsADirectoryError:
            print(colored("Error! No such file or directory.", "red"))  
            break       
    else:
        signature = input("Please enter the signature: ")

    rsatool.verification_data(message, signature)
        
    break