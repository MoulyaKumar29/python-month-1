class Employee:

    company = "ABC Company"


employee1 = Employee()
employee2 = Employee()

print(employee1.company)
print(employee2.company)

Employee.company = "XYZ Company"

print(employee1.company)
print(employee2.company)

