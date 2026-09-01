import json

student = {
    "name": "Moulya",
    "branch": "ECE",
    "marks": 90
}

with open("student_data.json", "w") as file:
    json.dump(student, file, indent=4)

print("Student data saved.")