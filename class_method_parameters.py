class Company:

    name = "ABC Company"

    @classmethod
    def change_company(cls, new_name):
        cls.name = new_name


print(Company.name)

Company.change_company("XYZ Company")

print(Company.name)