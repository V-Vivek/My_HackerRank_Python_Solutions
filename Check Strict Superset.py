# Question: https://www.hackerrank.com/challenges/py-check-strict-superset/problem

a = set(map(int, input().split()))
n = int(input())
result = True
for i in range(n):
    b = set(map(int, input().split()))
    if a == b:
        result = False
        break
    elif a.issuperset(b):
        continue
    else:
        result = False
        break
print(result)