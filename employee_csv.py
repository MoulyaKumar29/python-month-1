import csv

employees = [
    ["Name", "Department", "Salary"],
    ["Moulya", "Testing", 40000],
    ["Rahul", "Development", 50000],
    ["Anu", "HR", 35000]
]

with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(employees)

print("Employee data saved.")