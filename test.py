import calendar

weekday = ('MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY')
month, day, year = map(int, input().split())
print(weekday[calendar.weekday(year, month, day)])