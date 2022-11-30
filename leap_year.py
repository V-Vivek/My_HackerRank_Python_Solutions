# Question : https://www.hackerrank.com/challenges/write-a-function/problem
def is_leap(year):
    leap = False
    # To check century leap years
    if (year % 400 == 0) and (year % 100 == 0):
        leap = True
    # To check non-century leap years
    elif (year % 4 ==0) and (year % 100 != 0):
        leap = True
    
    return leap

year = int(input())
print(is_leap(year))
