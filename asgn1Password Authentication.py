import re
import hashlib


def is_strong_password(password):
    if len(password) < 8:
        return False
    
    if not re.search(r"[A-Z]", password):  
        return False
    
    if not re.search(r"[a-z]", password):  
        return False
    
    if not re.search(r"[0-9]", password):  
        return False
    
    if not re.search(r"[!@#$%^&*()_+=]", password):
        return False
    
    return True


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register():
    password = input("Create a strong password: ")
    
    if is_strong_password(password):
        hashed = hash_password(password)
        print(" Password registered successfully!")
        return hashed
    else:
        print(" Weak password! Try again.")
        return None

def login(stored_password):
    password = input("Enter your password: ")
    hashed = hash_password(password)
    
    if hashed == stored_password:
        print("Login successful!")
    else:
        print(" Incorrect password!")

# Main Program
stored_password = None

while stored_password is None:
    stored_password = register()

login(stored_password)