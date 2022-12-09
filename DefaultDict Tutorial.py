# Question: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

from collections import defaultdict
a = defaultdict(list)

n, m = map(int, input().split())
for i in range(1, n+1):
    a[input()].append(str(i))

for j in range(1, m+1):
    inp = input()
    if inp in a:
        print(' '.join(a[inp]))
    else:
        print(-1)
