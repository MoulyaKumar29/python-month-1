subjects = ["Python", "C", "Java"]
marks = [90, 85, 88]

result = {subject: mark for subject, mark in zip(subjects, marks)}

print(result)