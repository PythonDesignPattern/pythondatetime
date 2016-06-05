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
print(tomorrow)  # 2016-06-06 18:57:20.377898
print(yesterday)  # 2016-06-04 18:57:20.377898
print(after_45_minute)  # 2016-06-05 19:42:20.377898
print(now)  # 2016-06-05 18:57:20.377898
print(now.year)  # 2016
print(now.month)  # 6
print(now.day)  # 5
print(now.second)  # 20
print(now.microsecond)  # 377898

# Difference between `.now()` and `.today()`
# `.now()` takes timezone as an argument

print('%s/%s/%s' % (now.month, now.day, now.year))  # 6/5/2016
print('%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second))  # 6/5/2016 18:57:20

# To get today date at midnight
today_midnight = datetime.datetime.combine(datetime.date.today(), datetime.time())
print(today_midnight)  # 2016-06-05 00:00:00

# What day of the week today
# 0 : Monday
# 1 : Tuesday
# 2 : Wednesday
# .
# .
# 6 : Sunday
print(today_midnight.weekday())  # 6
print(now.timestamp())  # posix timestamp 1465133240.377898

# Visit for more info:
# https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior
print(now.strftime('%B %d'))  # June 05
# String from time
print(now.strftime('%m/%d/%y'))  # 06/05/16
# String parse into time, It is use for convert parse string into datetime
print(datetime.datetime.strptime('2016-05-06', '%Y-%m-%d'))  # 2016-05-06 00:00:00
# With time
print(datetime.datetime.strptime('2016-05-21 06:25', '%Y-%m-%d %H:%M'))  # 2016-05-21 06:25:00
