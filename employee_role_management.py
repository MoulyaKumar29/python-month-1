class Employee:

    company = "Developers Arena"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Company:", self.company)

    def show_role(self):
        print("Role: Employee")


class Developer(Employee):

    def show_role(self):
        print("Role: Developer")

    def show_skills(self):
        print("Skills: Python, Git, OOP")


class Tester(Employee):

    def show_role(self):
        print("Role: Tester")

    def show_skills(self):
        print("Skills: Testing, Python, SQL")


developer1 = Developer("Moulya", 45000)
tester1 = Tester("Anu", 40000)

print("Developer Details")
developer1.show_details()
developer1.show_role()
developer1.show_skills()

print()

print("Tester Details")
tester1.show_details()
tester1.show_role()
tester1.show_skills()