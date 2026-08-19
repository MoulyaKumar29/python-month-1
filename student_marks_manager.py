students = ["Moulya", "Anu", "Ravi", "Kiran"]
marks = [90, 85, 92, 78]

student_marks = {
    student: mark
    for student, mark in zip(students, marks)
}

passed_students = {
    student: mark
    for student, mark in student_marks.items()
    if mark >= 85
}

unique_marks = {
    mark
    for mark in marks
}

print("Student Marks:", student_marks)
print("Passed Students:", passed_students)
print("Unique Marks:", unique_marks)