class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, branch):
        super().__init__(name)
        self.branch = branch


student1 = Student("Moulya", "ECE")

print("Name:", student1.name)
print("Branch:", student1.branch)