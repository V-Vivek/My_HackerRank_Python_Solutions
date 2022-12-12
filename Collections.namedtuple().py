# Question: https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple

total = 0
N = int(input()) 
columns = input()
student = namedtuple('student', columns)
for _ in range(N):
    a, b, c, d = input().split()
    data = student(a, b, c, d)
    total += int(data.MARKS)

print(round(total/N, 2))