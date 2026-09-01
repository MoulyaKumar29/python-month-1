import re

text = "I have 10 apples and 20 oranges"

numbers = re.findall(r"\d+", text)

print(numbers)