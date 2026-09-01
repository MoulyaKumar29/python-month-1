import re

email = "moulya@gmail.com"

pattern = r"^[\w.-]+@[\w.-]+\.\w+$"

if re.match(pattern, email):
    print("Valid email")
else:
    print("Invalid email")