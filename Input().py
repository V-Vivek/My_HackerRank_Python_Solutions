# Question: https://www.hackerrank.com/challenges/input/problem

x, k = map(int, input().split())
p = input()
if eval(p) == k:
    print('True')
else:
    print('False')