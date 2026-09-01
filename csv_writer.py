import csv

with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Department", "Salary"])
    writer.writerow(["Moulya", "Testing", 40000])