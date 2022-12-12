# Question: https://www.hackerrank.com/challenges/word-order/problem

from collections import defaultdict
d1 = defaultdict(int)  # With the help of defaultdict we can eliminate the KeyError as default dict auto creates a key

n = int(input()) 
for _ in range(n):
    word = input()
    d1[word] += 1

print(len(d1.items()))
for x in d1.values():
    print(x, end = " ")