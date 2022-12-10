# Question: https://www.hackerrank.com/challenges/calendar-module/problem

import calendar

wday = ('MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY')
month, day, year = map(int, input().split())
print(wday[calendar.weekday(year, month, day)]) 
# calendar.weekday returns a integer specifying Weekday. We use that integer as index to get the weekday name