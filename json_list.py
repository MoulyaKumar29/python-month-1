import json

students = [
    {
        "name": "Moulya",
        "marks": 90
    },
    {
        "name": "Anu",
        "marks": 85
    }
]

json_data = json.dumps(students, indent=4)

print(json_data)