from datetime import datetime

now = datetime.now()

formatted_date = now.strftime("%d-%m-%Y")

print("Formatted Date:", formatted_date)