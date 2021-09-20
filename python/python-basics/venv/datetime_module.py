from datetime import date, time, datetime
print(date(year=2020, month=1, day=31))
print(time(hour=13, minute=14, second=31))
print(datetime(year=2020, month=1, day=31, hour=13, minute=14, second=31))
print(date.today())
print(datetime.now())
print(date.fromisoformat("2020-01-31"))
date_string = "01-31-2020 14:45:37"
format_string = "%m-%d-%Y %H:%M:%S"
print(datetime.strptime(date_string, format_string))
