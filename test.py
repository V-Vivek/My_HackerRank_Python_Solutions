t = int(input())
for i in range(t):
    a, b = input().split()
    try:
        print(int(a) // int(b))
    except ZeroDivisionError as err:
        print("Error Code:",err)
    except ValueError as err:
        print("Error Code:",err)

