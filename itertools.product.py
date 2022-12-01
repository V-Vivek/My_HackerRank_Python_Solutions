# Question: https://www.hackerrank.com/challenges/itertools-product/problem

A = list(map(int, input().split()))
B = list(map(int, input().split()))

result =[]
for i in A:
    for j in B:
        print(tuple([i,j]), end = " ")