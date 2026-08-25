class Person:

    def introduce(self):
        print("I am a person")


class Student(Person):
    pass


student1 = Student()

student1.introduce()