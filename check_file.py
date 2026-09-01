import os

if os.path.isfile("notes.txt"):
    print("It is a file.")
else:
    print("It is not a file.")