import rsatool
from termcolor import colored

    
## Main entry point    
while True:
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
        
    signature = input("Please enter the signature: ")
    rsatool.verification_data(message, signature)
        
    break