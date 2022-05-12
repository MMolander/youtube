"""
Dates are difficult to program with
Timezones, daylight savings
Representtation
Time is usually calculated using Unix epoch
"""

# Get the current year, month and day
from datetime import datetime, date
today = date.today()
print(today)

# Get the current year, month, day, hour, minute, second and ms
now = datetime.now()
print(now)

# Use the daytime constructor
someday = datetime (year=2023, month = 1, day = 10, hour = 16 )
print(someday)
print(type(someday))

span = someday - now
print(span)
print(type(span))
