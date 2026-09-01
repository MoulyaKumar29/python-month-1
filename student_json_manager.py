import json


FILE_NAME = "students.json"


def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student():
    name = input("Enter student name: ")
    branch = input("Enter branch: ")

    try:
        marks = float(input("Enter marks: "))

        student = {
            "name": name,
            "branch": branch,
            "marks": marks
        }

        students = load_students()
        students.append(student)

        save_students(students)

        print("Student added successfully.")

    except ValueError:
        print("Please enter valid marks.")


def show_students():
    students = load_students()

    if not students:
        print("No students found.")
        return

    for student in students:
        print()
        print("Name:", student["name"])
        print("Branch:", student["branch"])
        print("Marks:", student["marks"])


while True:

    print("\n--- Student JSON Manager ---")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_students()

    elif choice == "3":
        print("Program closed.")
        break

    else:
        print("Invalid choice.")