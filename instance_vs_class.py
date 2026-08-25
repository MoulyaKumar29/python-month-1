class Employee:

    company = "Tech Solutions"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


employee1 = Employee("Moulya", 40000)
employee2 = Employee("Rahul", 50000)

print(employee1.name)
print(employee1.salary)
print(employee1.company)

print(employee2.name)
print(employee2.salary)
print(employee2.company)