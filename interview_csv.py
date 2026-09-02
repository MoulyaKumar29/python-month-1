import csv

with open("interview_students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Marks"])
    writer.writerow(["Moulya", 90])

print("CSV created.")