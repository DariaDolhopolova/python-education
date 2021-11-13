import time
print(time.gmtime())
from time import time, ctime
print(time())
print(ctime(time()))

from time import struct_time
time_tuple = (2019, 2, 26, 7, 6, 55, 1, 57, 0)
time_obj = struct_time(time_tuple)
print(time_obj)

day_of_year = time_obj.tm_yday
print(day_of_year)

day_of_month = time_obj.tm_mday
print(day_of_month)

import time
import calendar
print(calendar.timegm(time.gmtime()))
print(time.localtime(1551448206.86196))
print(time.asctime())
