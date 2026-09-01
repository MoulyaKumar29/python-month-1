import json

student = {
    "name": "Moulya",
    "age": 22,
    "branch": "ECE"
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)