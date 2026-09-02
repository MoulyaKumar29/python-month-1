import json
from datetime import datetime


NOTES_FILE = "notes.json"
TASKS_FILE = "tasks.json"


class ProductivityManager:

    def __init__(self):
        self.notes = self.load_data(NOTES_FILE)
        self.tasks = self.load_data(TASKS_FILE)

    def load_data(self, filename):
        try:
            with open(filename, "r") as file:
                return json.load(file)

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            return []

    def save_data(self, filename, data):
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    def add_note(self):
        note = input("Enter note: ")

        self.notes.append({
            "note": note,
            "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        })

        self.save_data(NOTES_FILE, self.notes)

        print("Note saved successfully.")

    def show_notes(self):
        if not self.notes:
            print("No notes found.")
            return

        print("\n--- Notes ---")

        for index, item in enumerate(self.notes, start=1):
            print(index, ".", item["note"])
            print("Date:", item["date"])

    def add_task(self):
        task = input("Enter task: ")

        self.tasks.append({
            "task": task,
            "completed": False
        })

        self.save_data(TASKS_FILE, self.tasks)

        print("Task added successfully.")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return

        print("\n--- Tasks ---")

        for index, item in enumerate(self.tasks, start=1):

            status = "Completed" if item["completed"] else "Pending"

            print(index, ".", item["task"], "-", status)

    def complete_task(self):
        self.show_tasks()

        if not self.tasks:
            return

        try:
            task_number = int(input("Enter task number: "))

            if task_number < 1 or task_number > len(self.tasks):
                print("Invalid task number.")
                return

            self.tasks[task_number - 1]["completed"] = True

            self.save_data(TASKS_FILE, self.tasks)

            print("Task completed.")

        except ValueError:
            print("Please enter a valid number.")

    def calculator(self):

        try:
            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))

            print("\n1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")

            choice = input("Choose operation: ")

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

    def run(self):

        while True:

            print("\n==============================")
            print(" PERSONAL PRODUCTIVITY SUITE")
            print("==============================")

            print("1. Add Note")
            print("2. Show Notes")
            print("3. Add Task")
            print("4. Show Tasks")
            print("5. Complete Task")
            print("6. Calculator")
            print("7. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.add_note()

            elif choice == "2":
                self.show_notes()

            elif choice == "3":
                self.add_task()

            elif choice == "4":
                self.show_tasks()

            elif choice == "5":
                self.complete_task()

            elif choice == "6":
                self.calculator()

            elif choice == "7":
                print("Thank you for using Personal Productivity Suite.")
                break

            else:
                print("Invalid choice.")


manager = ProductivityManager()

manager.run()