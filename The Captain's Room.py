# Question: https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true

# Solution #1: Takes more time to execute
k = int(input())
room_number_list = list(map(int, input().split()))
unique_rooms = list(set(room_number_list))

for _ in unique_rooms:
    if room_number_list.count(_) != k:
        print(_)

# Optimized solution:

from collections import Counter

k = int(input())
room_count = dict(Counter(map(int, input().split())))

for k,v in room_count.items():
    if v == 1:
        print(k)