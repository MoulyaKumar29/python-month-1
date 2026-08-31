from datetime import datetime

now = datetime.now()

formatted_time = now.strftime("%H:%M:%S")

print("Formatted Time:", formatted_time)