numbers = [10, 20, 30, 40, 50]

smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print(smallest)