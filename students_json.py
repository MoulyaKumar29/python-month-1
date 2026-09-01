import json

students = [
    {"name": "Moulya", "marks": 90},
    {"name": "Anu", "marks": 85},
    {"name": "Ravi", "marks": 78}
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

print("Students saved.")