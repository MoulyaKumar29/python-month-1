def square(number):
    return number ** 2


def factorial(number):
    result = 1

    for i in range(1, number + 1):
        result *= i

    return result


def reverse_text(text):
    return text[::-1]


while True:

    print("\n--- Python Practice Toolkit ---")
    print("1. Square")
    print("2. Factorial")
    print("3. Reverse Text")
    print("4. Exit")

    choice = input("Enter choice: ")

    try:

        if choice == "1":
            number = int(input("Enter number: "))
            print("Square:", square(number))

        elif choice == "2":
            number = int(input("Enter number: "))

            if number < 0:
                raise ValueError("Negative numbers are not allowed.")

            print("Factorial:", factorial(number))

        elif choice == "3":
            text = input("Enter text: ")
            print("Reverse:", reverse_text(text))

        elif choice == "4":
            print("Program closed.")
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter a valid value.")