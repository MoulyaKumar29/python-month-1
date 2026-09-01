import re

text = "Apple,Mango,Banana,Orange"

fruits = re.split(",", text)

print(fruits)