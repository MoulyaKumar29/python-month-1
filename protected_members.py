class Employee:

    def __init__(self, salary):
        self._salary = salary


employee1 = Employee(40000)

print(employee1._salary)