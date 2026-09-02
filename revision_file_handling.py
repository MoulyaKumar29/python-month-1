with open("revision_notes.txt", "w") as file:
    file.write("Python revision is important.")

with open("revision_notes.txt", "r") as file:
    content = file.read()

print(content)