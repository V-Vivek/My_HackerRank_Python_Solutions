from collections import defaultdict
a = defaultdict(list)

n, m = map(int, input().split())
for i in range(1, n+1):
    a[input()].append(str(i))

for j in range(1, m+1):
    inp = input()
    if inp in a:
        print(' '.join(a[inp]))
    else:
        print(-1)

# from collections import defaultdict
# d = defaultdict(list)
# list1=[]
# n, m = map(int,input().split())
# for i in range(1, n+1):
#     d[input()].append(str(i))


# for i in range(m):
#     b = input()
#     if b in d: 
#         print(' '.join(d[b]))
#     else: 
#         print(-1)