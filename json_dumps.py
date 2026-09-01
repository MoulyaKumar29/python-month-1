import json

student = {
    "name": "Moulya",
    "age": 22,
    "branch": "ECE"
}

json_data = json.dumps(student)

print(json_data)