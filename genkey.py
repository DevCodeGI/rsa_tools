from rsatool import rsatool
from termcolor import colored
from getpass import getpass


## Main entry point
while True:
    rsatool = rsatool()
    
    # Ask the password to generate the key
    master_password = getpass("Enter new password: ")
    if master_password != getpass("Confirm new password: "):
        print(colored("Error: Password confirmation doesn't match the password!", "red"))
        break
    
    # Start generate key with password
    private_key, pem_private_key, public_key, pem_public_key = rsatool.generate_key(master_password)
    
    # Save the key into file
    rsatool.save_key(pem_private_key, pem_public_key)
    
    # Ask user to validate the key
    print()
    answer = input("Do you want to validate the private key (y/n)? ").lower()
    if answer == "y":
        validate_password = getpass("Enter your password: ")
        
        # Validate the key with password
        if rsatool.load_private_key(validate_password) is not None:
            print(colored("Private key identified.", "green"))

    break
                    