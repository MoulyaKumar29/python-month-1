student = {
    "name": "Moulya",
    "branch": "ECE",
    "year": 4,
    "marks":{
        "Python": 90,
        "C": 85,
        "Embedded C": 88
    }
}
student["marks"]["JavaScript"] = 92

student["marks"]["C"] = 90

for subject, mark in student["marks"].items():
    print(subject, mark)

if "Python" in student["marks"]:
    print("Python marks available")


student["marks"].pop("JavaScript")

print(student)

total = 0

for mark in student["marks"].values():
    total = total + mark

print("Total marks:", total)

average = total / len(student["marks"])

print("Average marks:", average)