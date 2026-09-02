import csv

students = [
    ["Name", "Branch", "Marks"],
    ["Moulya", "ECE", 90],
    ["Anu", "CSE", 85],
    ["Ravi", "ISE", 78]
]

with open("revision_students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("CSV file created.")