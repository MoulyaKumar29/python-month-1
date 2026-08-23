def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


while True:

    print("\n--- Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 5:
            print("Calculator closed.")
            break

        if choice not in [1, 2, 3, 4]:
            raise ValueError("Invalid choice.")

        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))

        if choice == 1:
            result = add(number1, number2)

        elif choice == 2:
            result = subtract(number1, number2)

        elif choice == 3:
            result = multiply(number1, number2)

        elif choice == 4:
            result = divide(number1, number2)

    except ValueError:
        print("Please enter valid numbers or a valid choice.")

    except ZeroDivisionError:
        print("Cannot divide by zero.")

    else:
        print("Result:", result)

    finally:
        print("Calculation completed.")