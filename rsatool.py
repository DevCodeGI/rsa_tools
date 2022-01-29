import hashlib, traceback, base64, binascii
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa, dsa, utils
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidSignature, UnsupportedAlgorithm
from termcolor import colored 

class rsatool:
    
    def __init__(self, key_name="id_rsa"):
        self.key_name = key_name

    # Generate the key with password
    def generate_key(self, master_password):
        try:
            private_key = rsa.generate_private_key(
                public_exponent = 65537,
                key_size = 4096,
                backend = default_backend()
            )
            pem_private_key = private_key.private_bytes(
                encoding = serialization.Encoding.PEM,
                format = serialization.PrivateFormat.PKCS8,
                encryption_algorithm = serialization.BestAvailableEncryption(
                    master_password.encode()
                )
            )
            public_key = private_key.public_key()
            pem_public_key = private_key.public_key().public_bytes(
                encoding = serialization.Encoding.PEM,
                format = serialization.PublicFormat.SubjectPublicKeyInfo
            )
        
            return private_key, pem_private_key, public_key, pem_public_key
        except Exception:
            print(colored("Error: The key can't generated.", "red"))
            traceback.print_exc()
        
    # Save the private and public key into file
    def save_key(self, pem_private_key, pem_public_key):
        try:
            with open(self.key_name + ".key", "w") as f:
                f.write(pem_private_key.decode())

            with open(self.key_name + ".pub", "w") as f:
                f.write(pem_public_key.decode())

            print(colored(f"Private and public key are generated successfully and saved into '{self.key_name}.key' and '{self.key_name}.pub'.", "green"))
        except Exception:
            print(colored("Error: The key can't save into file.", "red"))
            traceback.print_exc()

    # Load the private key with password
    def load_private_key(self, password):
        try:
            with open(self.key_name + ".key", "rb") as f:
                private_key = serialization.load_pem_private_key(
                    f.read(), 
                    password=password.encode()
                )
            if not isinstance(private_key, (rsa.RSAPublicKey, rsa.RSAPrivateKey,
                                            dsa.DSAPublicKey, dsa.DSAPrivateKey)):
                raise TypeError

            return private_key
        except FileNotFoundError:
            print(colored("Error! Private Key doesn't exist.", "red"))     
        except TypeError:
            print(colored("Error! Unsupported private key type.", "red"))
        except ValueError:
            print(colored("Error: Password doesn't match the private key.", "red"))
        except Exception:
            traceback.print_exc()

    # Load the public key
    def load_public_key(self):
        try:
            with open(self.key_name + ".pub", "rb") as f:
                public_key = serialization.load_pem_public_key(
                    f.read() 
                )
            if not isinstance(public_key, (rsa.RSAPublicKey, rsa.RSAPrivateKey,
                                        dsa.DSAPublicKey, dsa.DSAPrivateKey)):
                raise TypeError

            return public_key
        except FileNotFoundError:
            print(colored("Error! Public Key doesn't exist.", "red"))     
        except TypeError:
            print(colored("Error! Unsupported public key type.", "red"))
        except Exception:
            traceback.print_exc()

    # Signing the data
    def signing_data(self, message, password):
        try:
            # Load the private key
            private_key = load_private_key(password)
            
            if private_key is not None:
                chosen_hash = hashes.SHA256()
                hasher = hashes.Hash(chosen_hash)
                hasher.update(message.encode())
                digest = hasher.finalize()
                signature = private_key.sign(
                    digest,
                    padding.PSS(
                        mgf=padding.MGF1(hashes.SHA256()),
                        salt_length=padding.PSS.MAX_LENGTH
                    ),
                    utils.Prehashed(chosen_hash)
                )

                return base64.b64encode(signature).decode()
        except UnsupportedAlgorithm:
            print(colored("Error! Signature failed.", "red"))
        except Exception:
            traceback.print_exc()
        
    # Verification the data
    def verification_data(self, message, signature):
        try:
            # Load the public key
            public_key = load_public_key()

            if public_key is not None:
                chosen_hash = hashes.SHA256()
                hasher = hashes.Hash(chosen_hash)
                hasher.update(message.encode())
                digest = hasher.finalize()
                public_key.verify(
                    base64.b64decode(signature),
                    digest,
                    padding.PSS(
                        mgf=padding.MGF1(hashes.SHA256()),
                        salt_length=padding.PSS.MAX_LENGTH
                    ),
                    utils.Prehashed(chosen_hash)
                )

            print(colored("Signature identified.", "green"))
        except InvalidSignature:
            print(colored("Error! Signature verification failed.", "red"))
        except binascii.Error:
            print(colored("Error! Unsupported signature format.", "red"))
        except NameError:
            print(colored("Error! Invalid signature format.", "red"))       
        except Exception:
            traceback.print_exc()

    def encrypt(self, message):
        try:
            # Load the public key
            public_key = load_public_key()
            
            if public_key is not None:      
                ciphertext = public_key.encrypt(
                    message.encode(),
                    padding.OAEP(
                        mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),
                        label=None
                    )
                )
            
                return base64.b64encode(ciphertext).decode()
        except ValueError:
            print(colored("Error! Encryption failed.", "red"))
        except Exception:
            traceback.print_exc()
            
    def decrypt(self, ciphertext, password):
        try:
            # Load the private key
            private_key = load_private_key(password)
            
            if private_key is not None:            
                plaintext = private_key.decrypt(
                    base64.b64decode(ciphertext),
                    padding.OAEP(
                        mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),
                        label=None
                    )
                )
                
                return plaintext.decode()
        except ValueError:
            print(colored("Error! Decryption failed.", "red"))
        except binascii.Error:
            print(colored("Error! Unsupported encryption format.", "red"))
        except Exception:
            traceback.print_exc()