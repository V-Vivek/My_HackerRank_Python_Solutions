# k = 5
# room_number_list = [1, 2, 3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3, 2, 4, 1, 2, 5, 1, 4, 3, 6, 8, 4, 3, 1, 5, 6, 2]


from collections import Counter

k = int(input())
room_count = dict(Counter(map(int, input().split())))
print(room_count)

for k,v in room_count.items():
    if v == 1:
        print(k)