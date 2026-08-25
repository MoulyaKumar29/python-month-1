class Employee:

    company = "ABC Company"

    def __init__(self, name):
        self.name = name


employee1 = Employee("Moulya")
employee2 = Employee("Rahul")

print(employee1.company)
print(employee2.company)

Employee.company = "XYZ Company"

print(employee1.company)
print(employee2.company)