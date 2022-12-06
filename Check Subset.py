# Question: https://www.hackerrank.com/challenges/py-check-subset/problem

# Solution #1
t = int(input())

for i in range(t):
    len_a = int(input())
    a = set(map(int, input().split()))
    len_b = int(input())
    b = set(map(int, input().split()))
    
    list_a = list(a)
    for _ in list_a:
        if _ in b:
            continue
        else:
            print(False)
            break
    else:
        print(True)


# Solution #2

t = int(input())

for i in range(t):
    len_a = int(input())
    a = set(map(int, input().split()))
    len_b = int(input())
    b = set(map(int, input().split()))
    print(a.issubset(b))
