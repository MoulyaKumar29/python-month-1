import json

person = {
    "name": "Moulya",
    "age": 22,
    "city": "Mysore"
}

result = json.dumps(person)

print(result)