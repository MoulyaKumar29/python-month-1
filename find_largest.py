numbers = [25, 70, 15, 90, 45]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest:", largest)