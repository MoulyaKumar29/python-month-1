import json

json_data = '{"name": "Moulya", "age": 22}'

student = json.loads(json_data)

print(student)
print(student["name"])