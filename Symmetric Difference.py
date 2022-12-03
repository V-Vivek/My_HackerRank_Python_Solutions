# Question: https://www.hackerrank.com/challenges/symmetric-difference/problem

M = int(input())
s1 = set(map(int, input().split()))
N = int(input())
s2 = set(map(int, input().split()))

result = list((s1-s2).union(s2-s1))  # extract symmetric difference integers from two sets
result.sort() # sort the result list
for x in result:
    print(x)