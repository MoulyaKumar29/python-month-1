class Student:

    def __init__(self, name, branch):
        self.name = name
        self.branch = branch


student1 = Student("Moulya", "ECE")
student2 = Student("Anu", "CSE")

print(student1.name)
print(student1.branch)

print(student2.name)
print(student2.branch)