import rsatool
from termcolor import colored

    
## Main entry point    
while True:
    # Start to validation signature
    message = input("Please enter the message: ")
    signature = input("Please enter the signature: ")
    rsatool.verification_data(message, signature)
        
    break