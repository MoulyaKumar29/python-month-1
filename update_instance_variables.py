class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


employee1 = Employee("Rahul", 30000)

print("Before:", employee1.salary)

employee1.salary = 40000

print("After:", employee1.salary)