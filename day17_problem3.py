class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def update_salary(self, new_salary):
        self.salary = new_salary

    def show_salary(self):
        print("Salary:", self.salary)


employee1 = Employee("Anu", 35000)

employee1.update_salary(45000)

employee1.show_salary()