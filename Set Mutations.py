# Question: https://www.hackerrank.com/challenges/py-set-mutations/problem?isFullScreen=true

n = int(input())
A = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    command, count = input().split()
    other_set = set(map(int, input().split()))
    if command == 'update':
        A |= other_set
    elif command == 'intersection_update':
        A &= other_set
    elif command == 'difference_update':
        A -= other_set
    elif command == 'symmetric_difference_update':
        A ^= other_set

print(sum(A))