import re

text = "My age is 22"

result = re.findall(r"\d+", text)

print(result)