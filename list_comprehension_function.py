def is_vowel_start(word):
    return word[0].lower() in ('a', 'e', 'i', 'o','u')

fruits = ["apple", "banana", "orange", "grape", "mango"]

vowel_checks = [is_vowel_start(fruit) for fruit in fruits]

print(vowel_checks)