import csv

students = [
    ["Name", "Branch", "Marks"],
    ["Moulya", "ECE", 90],
    ["Anu", "CSE", 85],
    ["Ravi", "ISE", 78]
]

with open("students_output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("Student data saved.")