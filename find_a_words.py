import re

text = "Anu and Asha are attending an event"

words = re.findall(r"\bA\w*", text)

print(words)