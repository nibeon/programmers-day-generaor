import random
from datetime import datetime, date, timedelta

print("=============================", end='\n')
print("Programmer's Day Generator.", end='\n')
print("=============================", end='\n')

print("This is a program to determine the day of the programmer.")
print("This program is desirable to run on New Year's Eve after midnight!", end='\n')

# get year
this_year = datetime.today().year

print("Hello in ", this_year, " year!", end='\n')

# get nombers of days in year
if (int(this_year) % 4 == 0):
    days = 366
else:
    days = 365

# geerate number of day
programmer_day = random.randint(1,days)

# convert number of day to date
start_date = date(int(this_year), 1, 1)
res_date = start_date + timedelta(programmer_day - 1)
res = res_date.strftime("%d-%m-%Y")

# print result
print("In {0} year you celebrated Programmer's Day in {1} day of year.".format(this_year, programmer_day))
print("This day falls on: ", str(res),"\n")
print("Happy Programmer's Day! :-)")
