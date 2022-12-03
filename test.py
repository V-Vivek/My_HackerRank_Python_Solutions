s1 = {1, 2, 3, 4}
s2 = {1, 2, 5, 6}

result = list((s1-s2).union(s2-s1))
result.sort()
for x in result:
    print(x)