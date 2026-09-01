import os

filename = "notes.txt"

if os.path.exists(filename):
    print("File exists.")
else:
    print("File not found.")