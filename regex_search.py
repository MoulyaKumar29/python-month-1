import re

text = "Python is easy to learn"

result = re.search("easy", text)

if result:
    print("Pattern found")
else:
    print("Pattern not found")