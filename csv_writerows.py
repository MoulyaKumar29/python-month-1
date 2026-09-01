import csv

rows = [
    ["Name", "Marks"],
    ["Moulya", 90],
    ["Anu", 85],
    ["Ravi", 78]
]

with open("marks.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)