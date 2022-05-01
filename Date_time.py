from datetime import datetime
now = datetime.now()

print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print("")

day = now.day
hour = now.hour
minutes = now.minute

if day == 28:
    print("Today is the day")

'Getting the hour in real time can help us to make task in'
'a certain point of the day'