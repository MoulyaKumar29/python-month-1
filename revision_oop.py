class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show_details(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


student1 = Student("Moulya", 90)

student1.show_details()