class Employee:

    def work(self):
        print("Employee is working")


class Developer(Employee):

    def work(self):
        print("Developer is writing code")


class Tester(Employee):

    def work(self):
        print("Tester is testing software")


developer1 = Developer()
tester1 = Tester()

developer1.work()
tester1.work()