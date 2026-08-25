class Student:

    school = "GSSSIETW"

    def __init__(self, name):
        self.name = name


student1 = Student("Moulya")
student2 = Student("Anu")

print(student1.name, student1.school)
print(student2.name, student2.school)