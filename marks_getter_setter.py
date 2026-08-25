class Student:

    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        self.__marks = marks


student1 = Student(75)

print("Old Marks:", student1.get_marks())

student1.set_marks(90)

print("New Marks:", student1.get_marks())