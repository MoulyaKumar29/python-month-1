from datetime import datetime

now = datetime.now()

formatted = now.strftime("%d-%m-%Y")

print("Date:", formatted)