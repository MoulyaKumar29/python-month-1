import csv

with open("students_data.csv", "w", newline="") as file:

    fieldnames = ["Name", "Branch", "Marks"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    writer.writerow({
        "Name": "Moulya",
        "Branch": "ECE",
        "Marks": 90
    })