#   import statements are used to import pre-defined or user-defined modules.
# import datetime
# alternatively, you can also write
from datetime import datetime, date
import calendar
import pytz

# current date
now = datetime.now()
print(f"Current date & time is: {now}")

# Get today's date
today = date.today()
print('Today:', today)

# extract attributes
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)


# Extract time from datetime object
t = datetime.now().time()
print('Time is:', t)

print('Hours', t.hour)
print('Minutes', t.minute)
print('Seconds', t.second)
print('Microseconds', t.microsecond)

# now, let's print calender
print(calendar.month(today.year, today.month))

print("List of all country codes:")
for country in pytz.country_names:
    print(country)