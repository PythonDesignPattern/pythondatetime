import datetime
"""
Create by Soham Navadiya
5-JUN-2016

"""
MIN_45 = 45

now = datetime.datetime.now()
tomorrow = now + datetime.timedelta(days=1)
yesterday = now - datetime.timedelta(days=1)  # --tomorrow = now + datetime.timedelta(days=-1)
after_45_minute = now + datetime.timedelta(minutes=MIN_45)
print(tomorrow)
print(yesterday)
print(after_45_minute)
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.second)
print(now.microsecond)

# Difference between `.now()` and `.today()`
# `.now()` takes timezone as an argument

print('%s/%s/%s' % (now.month, now.day, now.year))
print('%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second))

# To get today date at midnight
today_midnight = datetime.datetime.combine(datetime.date.today(), datetime.time())
print(today_midnight)

# What day of the week today
# 0 : Monday
# 1 : Tuesday
# 2 : Wednesday
# .
# .
# 6 : Sunday
print(today_midnight.weekday())
print(now.timestamp())  # posix timestamp
