N = int(input())
arr = set(map(float, input().split()))

avg = sum(arr) / len(arr)
print(round(avg, 3))