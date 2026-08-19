students = [
    ("Kiran", 80),
    ("Anjali", 95),
    ("Moulya", 88),
    ("Ravi", 72)
]

result = sorted(students, key=lambda x: x[1], reverse=True)

print(result)