import os

FILE_NAME = "notes.txt"

def add_note():
    note = input("Enter your note: ")
    with open(FILE_NAME, "a") as file:
        file.write(note + "\n")
    print("Note saved.")

def view_notes():
    if not os.path.exists(FILE_NAME):
        print("No notes yet.")
        return
    with open(FILE_NAME, "r") as file:
        print(file.read())

while True:
    choice = input("\n1. Add Note\n2. View Notes\n3. Exit\nChoose: ")
    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        break
    else:
        print("Invalid choice.")