from collections import defaultdict
d1 = defaultdict(int)

n = int(input()) 
for _ in range(n):
    word = input()
    d1[word] += 1

print(len(d1.items()))
for x in d1.values():
    print(x)