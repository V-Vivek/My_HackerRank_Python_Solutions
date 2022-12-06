# Question: https://www.hackerrank.com/challenges/py-set-difference-operation/problem?isFullScreen=true

n = int(input())
english = set(map(int, input().split()))
b = int(input())
french = set(map(int, input().split()))

# Solution #1

english = english.difference(french)
print(len(english))

# Solution #2

# english = english - french
# print(len(english))