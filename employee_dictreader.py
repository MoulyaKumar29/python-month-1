import csv

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)

    for employee in reader:
        print(
            employee["Name"],
            "-",
            employee["Department"],
            "-",
            employee["Salary"]
        )