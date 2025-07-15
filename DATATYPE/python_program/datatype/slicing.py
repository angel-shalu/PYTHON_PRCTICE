# String Slicing 
my_string = "Python Programming"

print(my_string[0:6])    # Characters from index 0 to 5 → 'Python'
print(my_string[:6])     # Same as above (start index omitted)
print(my_string[7:])     # From index 7 to end → 'Programming'
print(my_string[::2])    # Every 2nd character → 'Pto rgamn'
print(my_string[::-1])   # Reverse the string → 'gnimmargorP nohtyP'


# List Slicing
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(my_list[2:5])     # Elements from index 2 to 4 → [3, 4, 5]
print(my_list[:4])      # From start to index 3 → [1, 2, 3, 4]
print(my_list[5:])      # From index 5 to end → [6, 7, 8, 9]
print(my_list[::3])     # Every 3rd element → [1, 4, 7]
print(my_list[::-1])    # Reverse the list → [9, 8, 7, ..., 1]


# Tuple Slicing
my_tuple = (10, 20, 30, 40, 50, 60)

print(my_tuple[1:4])   # Elements from index 1 to 3 → (20, 30, 40)
print(my_tuple[:3])    # First 3 elements → (10, 20, 30)
print(my_tuple[3:])    # From index 3 to end → (40, 50, 60)
print(my_tuple[::-1])  # Reverse the tuple → (60, 50, 40, 30, 20, 10)

