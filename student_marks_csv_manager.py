import csv


FILE_NAME = "students.csv"


def add_student():
    name = input("Enter name: ")
    branch = input("Enter branch: ")

    try:
        marks = float(input("Enter marks: "))
    except ValueError:
        print("Please enter valid marks.")
        return

    file_exists = False

    try:
        with open(FILE_NAME, "r"):
            file_exists = True
    except FileNotFoundError:
        file_exists = False

    with open(FILE_NAME, "a", newline="") as file:
        fieldnames = ["Name", "Branch", "Marks"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "Name": name,
            "Branch": branch,
            "Marks": marks
        })

    print("Student added successfully.")


def show_students():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)

            found = False

            for student in reader:
                found = True

                print()
                print("Name:", student["Name"])
                print("Branch:", student["Branch"])
                print("Marks:", student["Marks"])

            if not found:
                print("No students found.")

    except FileNotFoundError:
        print("No student file found.")


while True:

    print("\n--- Student Marks CSV Manager ---")
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