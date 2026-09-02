import json


NOTES_FILE = "notes.json"


def load_notes():
    try:
        with open(NOTES_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=4)


def add_note():
    note = input("Enter note: ")

    notes = load_notes()
    notes.append(note)

    save_notes(notes)

    print("Note saved.")


def show_notes():
    notes = load_notes()

    if not notes:
        print("No notes found.")
        return

    print("\nNotes:")

    for index, note in enumerate(notes, start=1):
        print(index, ".", note)


def calculator():
    try:
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))

        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        choice = input("Enter choice: ")

        if choice == "1":
            result = number1 + number2

        elif choice == "2":
            result = number1 - number2

        elif choice == "3":
            result = number1 * number2

        elif choice == "4":
            result = number1 / number2

        else:
            print("Invalid choice.")
            return

        print("Result:", result)

    except ValueError:
        print("Please enter valid numbers.")

    except ZeroDivisionError:
        print("Cannot divide by zero.")


while True:

    print("\n--- Personal Productivity Suite ---")
    print("1. Add Note")
    print("2. Show Notes")
    print("3. Calculator")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_note()

    elif choice == "2":
        show_notes()

    elif choice == "3":
        calculator()

    elif choice == "4":
        print("Program closed.")
        break

    else:
        print("Invalid choice.")