class Student:

    def __init__(self, name, branch, marks):
        self.name = name
        self.branch = branch
        self.marks = marks

    def show_details(self):
        print("Name:", self.name)
        print("Branch:", self.branch)
        print("Marks:", self.marks)

    def check_result(self):
        if self.marks >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")


student1 = Student("Moulya", "ECE", 85)
student2 = Student("Anu", "CSE", 72)

print("Student 1")
student1.show_details()
student1.check_result()

print()

print("Student 2")
student2.show_details()
student2.check_result()