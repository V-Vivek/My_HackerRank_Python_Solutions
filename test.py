n = int(input())
english = set(map(int, input().split()))
b = int(input())
french = set(map(int, input().split()))

# Solution #1

# english = english.symmetric_difference(french)
# print(len(english))

# Solution #2

english = (english - french).union(french - english)
print(len(english))