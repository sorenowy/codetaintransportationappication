import re  

def validate_email(email) -> bool:  
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):  
        return True  
    return False  

def validate_password_policy(password) -> bool:
    specialCharacters = [ '$', '@', "!", "#", '%', '^', '&', '*', '(', ')', '_', '-', '?', '.', ',', '[', ']' ]
    result = True
    if len(password) < 8:
        result = False
        return result
    if not any(char.isdigit() for char in password):
        result = False
        return result
    if not any(char.isupper() for char in password):
        result = False
        return result
    if not any(char.islower() for char in password):
        result = False
        return result
    if not any(char in specialCharacters for char in password):
        result = False
        return result
    if result:
        return result
    