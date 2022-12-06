n = int(input())
english = set(map(int, input().split()))
b = int(input())
french = set(map(int, input().split()))

# english = english.difference(french)
# print(len(english))

# Solution #2

english = english - french
print(len(english))