# Question: https://www.hackerrank.com/challenges/python-sort-sort/problem

# Take required inputs
n, m = map(int, input().split())
nested_list =[]
for _ in range(n):
    nested_list.append(list(map(int, input().split())))
k = int(input())

nested_list.sort(key = lambda x : x[k]) # sort using the kth attribute
for list in nested_list:
    for item in list:
        print(item, end=" ")
    print()