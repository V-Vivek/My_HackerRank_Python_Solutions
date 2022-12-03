# Question: https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations
s, k = input().split()
s = list(list(permutations(s))[0]) # split each character of the string
s.sort()
k = int(k)


for i in permutations(s, k): # pass sorted string & k to generate permutations
    for j in i:
        print(j, end ='')
    print()