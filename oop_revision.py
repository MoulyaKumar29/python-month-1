class Calculator:

    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def add(self):
        return self.number1 + self.number2

    def multiply(self):
        return self.number1 * self.number2


calculator1 = Calculator(10, 20)

print("Addition:", calculator1.add())
print("Multiplication:", calculator1.multiply())