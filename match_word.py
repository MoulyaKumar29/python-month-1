import re

text = "Python programming"

result = re.match("Python", text)

if result:
    print("Matched at beginning")
else:
    print("Not matched")