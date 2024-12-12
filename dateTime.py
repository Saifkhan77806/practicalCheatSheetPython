from datetime import datetime, timedelta

now = datetime.now()

print("To print the date and time", now)

print(f"to print the today's date {now.strftime("%d")}:{now.strftime("%m")}:{now.strftime("%y")}")
print(f"to print the time {now.strftime("%H")}:{now.strftime("%M")}:{now.strftime("%S")}")
