from datetime import date, timedelta

today = date.today()

future_date = today + timedelta(days=7)

print("Today:", today)
print("After 7 Days:", future_date)