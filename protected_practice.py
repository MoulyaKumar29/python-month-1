class Employee:

    def __init__(self, department):
        self._department = department

    def show_department(self):
        print("Department:", self._department)


employee1 = Employee("Testing")

employee1.show_department()