class Employee:

    company = "Developers Arena"
    employee_count = 0

    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

        Employee.employee_count += 1

    def show_details(self):
        print("Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.salary)
        print("Company:", self.company)

    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name

    @classmethod
    def show_employee_count(cls):
        print("Total Employees:", cls.employee_count)


employee1 = Employee("Moulya", "Electronics", 40000)
employee2 = Employee("Rahul", "Testing", 35000)

print("Employee 1")
employee1.show_details()

print()

print("Employee 2")
employee2.show_details()

print()

Employee.show_employee_count()

Employee.change_company("Tech Solutions")

print()

print("After Company Name Change")

employee1.show_details()
employee2.show_details()