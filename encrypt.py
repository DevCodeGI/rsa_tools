from rsatool import rsatool
from termcolor import colored

#Define variables
file_name = None


## Main entry point    
while True:
    # Create object
    rsatool = rsatool()
    
    # Start to encrypt data
    answer = input("Do you want to encrypt the plaintext from file (y/n)? ").lower()
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
        message = input("Please enter the message to encrypt: ")
 
    ciphertext = rsatool.encrypt(message)
    if ciphertext is not None:
        print()
        print("-----BEGIN ENCRYPTED-----\n"
                + ciphertext
                + "\n-----END ENCRYPED-----")
        
        # Ask to save into file
        print()
        answer = input("Do you want to save into file (y/n)? ").lower()
        if answer == "y":
            if file_name is None:
                file_name = "noname"
            with open(file_name + ".enc", "w") as f:
                f.write(ciphertext)
                print(colored(f"Ciphertext saved into '{file_name}.enc'.", "green"))
                
    break