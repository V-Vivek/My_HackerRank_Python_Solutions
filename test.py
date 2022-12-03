from itertools import permutations
s, k = input().split()
s = list(list(permutations(s))[0])
s.sort()
print(s)
k = int(k)


for i in permutations(s, k):
    for j in i:
        print(j, end ='')
    print()