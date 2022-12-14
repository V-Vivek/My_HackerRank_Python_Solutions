# Question: https://www.hackerrank.com/challenges/no-idea/problem

happiness = 0
n, m = map(int, input().split())
arr = map(int, input().split())

a = set(map(int, input().split()))
b = set(map(int, input().split()))

for i in arr:
    if i in a:
        happiness += 1
    elif i in b:
        happiness -= 1

print(happiness)