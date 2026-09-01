import os

if not os.path.exists("Practice"):
    os.mkdir("Practice")
    print("Folder created.")
else:
    print("Folder already exists.")