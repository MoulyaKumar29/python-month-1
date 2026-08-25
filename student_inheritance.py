class Person:

    def show_name(self):
        print("Name: Moulya")


class Student(Person):

    def show_branch(self):
        print("Branch: ECE")


student1 = Student()

student1.show_name()
student1.show_branch()