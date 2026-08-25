class Employee:

    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary


employee1 = Employee(40000)

print("Salary:", employee1.get_salary())

employee1.set_salary(50000)

print("Updated Salary:", employee1.get_salary())