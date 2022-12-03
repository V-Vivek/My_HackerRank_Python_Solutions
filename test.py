from collections import Counter

X = int(input())
available_shoes = dict(Counter(map(int, input().split())))
N = int(input())
earnings = 0

for i in range(N):
    shoe_size_required, shoe_price = map(int, input().split())
    if available_shoes.get(shoe_size_required) != None:
        if available_shoes.get(shoe_size_required) > 0:
            earnings += shoe_price
            available_shoes[shoe_size_required] -= 1

print(available_shoes)
print(earnings)

'''
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
'''

