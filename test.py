n = int(input())
english = set(map(int, input().split()))
b = int(input())
french = set(map(int, input().split()))

english = english.intersection(french)
print(len(english))