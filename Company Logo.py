# Question: https://www.hackerrank.com/challenges/most-commons/problem

from collections import Counter
s = 'ccbbbbaade'

keys = list(dict(Counter(s)).keys())
values = list(dict(Counter(s)).values())
items = list(dict(Counter(s)).items())

func1 = lambda x: x[1]
items.sort()

items.sort(key=func1, reverse=True)

i = 0
while i < 3:
    print(items[i][0], items[i][1])
    i += 1