import json

student = {
    "name": "Moulya",
    "branch": "ECE",
    "marks": 90
}

with open("revision_student.json", "w") as file:
    json.dump(student, file, indent=4)

with open("revision_student.json", "r") as file:
    data = json.load(file)

print(data)