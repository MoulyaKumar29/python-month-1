import json

data = {
    "name": "Moulya",
    "skill": "Python"
}

json_data = json.dumps(data)

print(json_data)