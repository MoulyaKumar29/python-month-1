import json

data = '{"name": "Anu", "age": 21, "branch": "CSE"}'

person = json.loads(data)

print(person)
print(person["name"])