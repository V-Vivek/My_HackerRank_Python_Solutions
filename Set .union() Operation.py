# Question: https://www.hackerrank.com/challenges/py-set-union/problem?isFullScreen=true

n = int(input())
english = set(map(int, input().split()))
b = int(input())
french = set(map(int, input().split()))

english = english.union(french)
print(len(english))