class Student:

    school = "ABC College"

    def __init__(self, name):
        self.name = name


student1 = Student("Moulya")
student2 = Student("Anu")

print(student1.name)
print(student1.school)

print(student2.name)
print(student2.school)