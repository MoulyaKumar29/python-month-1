class Student:

    school = "ABC College"

    @classmethod
    def show_school(cls):
        print("School:", cls.school)


Student.show_school()