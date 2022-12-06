# Question: https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true

k = int(input())
room_number_list = list(map(int, input().split()))
unique_rooms = list(set(room_number_list))

for _ in unique_rooms:
    if room_number_list.count(_) != k:
        print(_)