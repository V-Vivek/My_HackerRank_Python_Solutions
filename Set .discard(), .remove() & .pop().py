# Question: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

n = int(input())
s = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    command = input()

    if command[:7] == 'discard':
        s.discard(int(command[8:]))

    elif command[:6] == 'remove':
        s.remove(int(command[7:]))

    else:
        s.pop()

print(sum(s))