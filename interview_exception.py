try:
    number = int(input("Enter number: "))
    print(100 / number)

except ValueError:
    print("Invalid input.")

except ZeroDivisionError:
    print("Cannot divide by zero.")