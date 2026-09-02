import re

text = "My phone numbers are 9876543210 and 8765432109"

numbers = re.findall(r"\b[6-9]\d{9}\b", text)

print(numbers)