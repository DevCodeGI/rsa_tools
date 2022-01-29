from rsatool import rsatool
import os
from termcolor import colored
from getpass import getpass

#Define variables
file_name = None


## Main entry point    
while True:
    # Create object
    rsatool = rsatool()
    
    # Start to decrypt data
    answer = input("Do you want to decrypt from file (y/n)? ").lower()
    if answer == "y":
        file_name = input("Enter the file name? ")
        try:
            with open(file_name, "r") as f:
                ciphertext = f.read()
        except FileNotFoundError:
            print(colored("Error! No such file or directory.", "red"))  
            break   
    else:    
        ciphertext = input("Please enter the ciphertext: ")
    
    password = getpass("Enter your password: ")    
    plaintext = rsatool.decrypt(ciphertext, password)
    if plaintext is not None:
        print()
        print("-----BEGIN PLAINTEXT-----\n"
                + plaintext
                + "\n-----END PLAINTEXT-----")
        
        if file_name is not None:
            print()
            answer = input("Do you want to save into file (y/n)? ").lower()
            if answer == "y":
                with open(os.path.splitext(file_name)[0] + ".dec", "w") as f:
                    f.write(plaintext)
                    print(colored(f"Plaintext saved into '{os.path.splitext(file_name)[0]}.dec'.", "green"))
        
    break