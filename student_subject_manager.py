student_subjects = ("Python", "Embedded Systems", "Digital Electronics", "Computer Networks", "Microcontrollers")

for student_subject in student_subjects:
    print(student_subject)

print(len(student_subjects))

student_skills = {"Python", "C", "Embedded C", "Verilog"}

print(student_skills)

student_skills.add("HTML")

print(student_skills)

student_skills.remove("Verilog")

print(student_skills)

other_student_skills = {"Python", "Java", "HTML"}

print(other_student_skills)

print(student_skills & other_student_skills)