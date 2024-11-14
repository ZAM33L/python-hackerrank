k = int(input())
room_number_list = list(map(int, input().split()))
room_number_set = set(room_number_list)
room_number_list_sum = sum(room_number_list)
room_number_set_sum = sum(room_number_set) * k
diff = room_number_set_sum - room_number_list_sum
for i in room_number_set:
    if diff == ((k - 1) * i):
        print(i)
        break

"""
from collections import Counter

# Read inputs
k = int(input())
room_numbers = list(map(int, input().split()))

# Count occurrences of each room number
room_count = Counter(room_numbers)

# Find and print the captain's room (the one that appears exactly once)
for room, count in room_count.items():
    if count == 1:
        print(room)
        break
        
"""