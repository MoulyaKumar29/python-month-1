class Student:

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)


student1 = Student("Moulya")

student1.show_name()