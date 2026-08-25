class Student:

    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        self.__marks = marks


student1 = Student(80)

print(student1.get_marks())

student1.set_marks(90)

print(student1.get_marks())