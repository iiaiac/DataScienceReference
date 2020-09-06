

#A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

#1- Import the datetime module and display the current date:

import datetime
x = datetime.datetime.now()
print(x)

#Return the year and name of weekday:
#Setting the timezone

import datetime
import pytz

x = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))

print(x)
print(x.year)
print(x.strftime("%A"))

#Create a date object:

import datetime

x = datetime.datetime(2020, 8, 20)

print(x)

#The strftime() Method
#The datetime object has a method for formatting date objects into readable strings. The method is called strftime(), and 
#it takes one parameter, format, to specify the format of the returned string:

#Display the name of the week:

import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%A"))

#Directive	Description	
#%a	        Weekday, short version	Wed	
#%A	        Weekday, full version	Wednesday	
#%w	        Weekday as a number 0-6, 0 is Sunday	
#%d	        Day of month 01-31	
#%b	        Month name, short version	
#%B       	Month name, full version	
#%m	        Month as a number 01-12		
#%y	        Year, short version, without century	
#%Y       	Year, full version		
#%H       	Hour 00-23		
#%I       	Hour 00-12		
#%p	        AM/PM	PM	
#%M	        Minute 00-59		
#%S	        Second 00-59		
#%f	        Microsecond 000000-999999	
#%z	        UTC offset	
#%Z	        Timezone	
#%j	        Day number of year 001-366	
#%U       	Week number of year, Sunday as the first day of week, 00-53		
#%W	        Week number of year, Monday as the first day of week, 00-53	
#%c	        Local version of date and time		
#%x	        Local version of date	
#%X	        Local version of time	
#%%	        A % character	%

import datetime

x = datetime.datetime.now()

print(x.strftime("%Y"))

#timedeltas
#You can use datetime to perform basic arithmetic on date values via the timedelta class.
#Subtracting dates produces a timedelta, and a timedelta can be added or subtracted from a date to produce another date. 
#The internal values for a timedelta are stored in days, seconds, and microseconds.

import datetime


print ("microseconds:", datetime.timedelta(microseconds=1))
print ("milliseconds:", datetime.timedelta(milliseconds=1))
print ("seconds     :", datetime.timedelta(seconds=1))
print ("minutes     :", datetime.timedelta(minutes=1))
print ("hours       :", datetime.timedelta(hours=1))
print ("days        :", datetime.timedelta(days=1))
print ("weeks       :", datetime.timedelta(weeks=1))

#Date Arithmetic
import datetime

today = datetime.date.today()
print ('Today    :', today)

one_day = datetime.timedelta(days=1)
print ('One day  :', one_day)

yesterday = today - one_day
print ('Yesterday:', yesterday)

tomorrow = today + one_day
print ('Tomorrow :', tomorrow)

print ('tomorrow - yesterday:', tomorrow - yesterday)
print ('yesterday - tomorrow:', yesterday - tomorrow)