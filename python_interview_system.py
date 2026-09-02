questions = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "answer": "def"
    },
    {
        "question": "Which keyword is used to create a class?",
        "answer": "class"
    },
    {
        "question": "Which data type stores key-value pairs?",
        "answer": "dictionary"
    },
    {
        "question": "Which keyword is used to handle exceptions?",
        "answer": "try"
    },
    {
        "question": "Which method is the constructor in Python?",
        "answer": "__init__"
    }
]


score = 0

print("--- Python Interview Practice ---")

for item in questions:

    print()
    print(item["question"])

    user_answer = input("Answer: ").strip().lower()

    if user_answer == item["answer"].lower():
        print("Correct.")
        score += 1
    else:
        print("Wrong.")
        print("Correct answer:", item["answer"])


print()
print("Final Score:", score, "/", len(questions))