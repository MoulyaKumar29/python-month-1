class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def show_balance(self):
        print("Balance:", self.__balance)


account1 = BankAccount(25000)

account1.show_balance()