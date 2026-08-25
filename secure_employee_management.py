from abc import ABC, abstractmethod


class Employee(ABC):

    company = "Tech Solutions"

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Salary cannot be negative.")

    def show_details(self):
        print("Name:", self.name)
        print("Salary:", self.__salary)
        print("Company:", self.company)

    @abstractmethod
    def show_role(self):
        pass


class Developer(Employee):

    def show_role(self):
        print("Role: Developer")


class Tester(Employee):

    def show_role(self):
        print("Role: Tester")


developer1 = Developer("Moulya", 45000)
tester1 = Tester("Anu", 40000)

print("Developer Details")
developer1.show_details()
developer1.show_role()

print()

print("Tester Details")
tester1.show_details()
tester1.show_role()

print()

developer1.set_salary(50000)

print("Updated Developer Salary:", developer1.get_salary())