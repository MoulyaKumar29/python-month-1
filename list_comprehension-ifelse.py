words = ["cat", "elephant", "dog", "hippopotamus", "ant"]

letters = ["long" if len(n) > 3 else "short" for n in words]

print(letters)