import datetime
now = datetime.datetime.now()
time = now.strftime("%H:%M")
midnight = datetime.time(hour=11, minute=15).strftime("%H:%M")
print(midnight)