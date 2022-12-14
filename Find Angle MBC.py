# Question: https://www.hackerrank.com/challenges/find-angle/problem

import math

a = int(input())
b = int(input())

print(round(math.degrees(math.atan(a/b))),chr(176), sep='')

# math.atan() calculates the tan inverse