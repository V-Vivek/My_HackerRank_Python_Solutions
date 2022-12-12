# Question: https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple

total = 0
N = int(input()) 
columns = input()
for i, column_name in enumerate(columns.split()):
    if column_name == 'ID':
        id = i
    elif column_name == 'MARKS':
        marks = i
    elif column_name == 'CLASS':
        cls = i
    else:
        name = i

student = namedtuple('student', columns)
for _ in range(N):
    a, b, c, d = input().split()
    data = student(a, b, c, d)
    total += int(data[marks])

print(round(total/N, 2))