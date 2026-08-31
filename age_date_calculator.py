from datetime import date, timedelta

birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))

birth_date = date(birth_year, birth_month, birth_day)
today = date.today()

age = today.year - birth_date.year

if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1

next_birthday = date(today.year, birth_month, birth_day)

if next_birthday < today:
    next_birthday = date(today.year + 1, birth_month, birth_day)

days_until_birthday = (next_birthday - today).days

print("Birth Date:", birth_date)
print("Current Date:", today)
print("Age:", age)
print("Days Until Next Birthday:", days_until_birthday)