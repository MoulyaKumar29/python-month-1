import re

text = "Python programming"

result = re.match("Python", text)

if result:
    print("Matched")
else:
    print("Not matched")