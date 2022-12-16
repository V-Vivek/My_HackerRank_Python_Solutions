
# Question: https://www.hackerrank.com/challenges/piling-up/problem

t = int(input())
for i in range(t):
    n = int(input())
    blocks = list(map(int, input().split()))
    oldtemp = max(blocks)
    possible = 1
    i = 0
    while i < len(blocks):
        if blocks[0] >= blocks[-1]:
            temp = blocks.pop(0)
        else:
            temp = blocks.pop(-1)
        
        if temp > oldtemp:
            print('No')
            possible = 0
            break
        else:
            oldtemp = temp

        i += 1

    if possible:
        print('Yes')
