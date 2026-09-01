import re

def validate_email(email):
    pattern = r"^[\w.-]+@[\w.-]+\.\w+$"

    if re.match(pattern, email):
        return True

    return False

def validate_phone(phone):
    pattern = r"^[6-9]\d{9}$"

    if re.match(pattern, phone):
        return True

    return False


email = input("Enter your email: ")
phone = input("Enter your phone number: ")

if validate_email(email):
    print("Valid email")
else:
    print("Invalid email")

if validate_phone(phone):
    print("Valid phone number")
else:
    print("Invalid phone number")