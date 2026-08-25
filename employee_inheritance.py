class Person:

    def show_name(self):
        print("Name: Rahul")


class Employee(Person):

    def show_job(self):
        print("Job: Software Engineer")


employee1 = Employee()

employee1.show_name()
employee1.show_job()