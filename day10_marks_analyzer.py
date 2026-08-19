marks = [45, 78, 92, 35, 88, 60, 25]

squared_marks = list(map(lambda x: x ** 2, marks))

passed_marks = list(filter(lambda x: x >= 50, marks))

sorted_marks = sorted(marks, key=lambda x: x, reverse=True)

print("Squared Marks:", squared_marks)
print("Passed Marks:", passed_marks)
print("Marks Highest to Lowest:", sorted_marks)