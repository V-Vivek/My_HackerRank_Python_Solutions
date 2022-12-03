# Question: https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

X = int(input()) # Total no. of shoes
available_shoes = dict(Counter(map(int, input().split()))) # Get dictionary with key = shoe size & value = no. of shoes of that size
N = int(input()) # no. of customers
earnings = 0

for i in range(N):
    shoe_size_required, shoe_price = map(int, input().split()) # customer request in sequential manner
    if available_shoes.get(shoe_size_required) != None: # check if shoe size exists
        if available_shoes.get(shoe_size_required) > 0: # check if shoe size available
            earnings += shoe_price # update earnings
            available_shoes[shoe_size_required] -= 1 # update available shoe count

print(earnings)