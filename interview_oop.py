class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(self.name, self.salary)


employee1 = Employee("Moulya", 40000)

employee1.show_details()