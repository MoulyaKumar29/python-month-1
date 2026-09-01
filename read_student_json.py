import json

with open("student_data.json", "r") as file:
    student = json.load(file)

print("Name:", student["name"])
print("Branch:", student["branch"])
print("Marks:", student["marks"])