N, X = map(int, input().split())
z = []
for i in range(X):
    temp = list(map(float, input().split()))
    if i == 0:
        z = temp
    else:
        z = zip(z, temp)
        print(list(z))
