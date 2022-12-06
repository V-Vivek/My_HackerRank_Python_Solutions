k = 5
room_number_list = [1, 2, 3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3, 2, 4, 1, 2, 5, 1, 4, 3, 6, 8, 4, 3, 1, 5, 6, 2]
unique_rooms = list(set(room_number_list))

for _ in unique_rooms:
    if room_number_list.count(_) != k:
        print(_)