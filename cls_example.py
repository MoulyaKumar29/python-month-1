class Company:

    name = "Tech Solutions"

    @classmethod
    def show_company(cls):
        print("Company:", cls.name)


Company.show_company()