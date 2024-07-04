import random

def rand_shuffle(data):
    i = len(data)
    for d in range(i):
        rand_index = random.randint(0, i - 1)
        data[d], data[rand_index] = data[rand_index], data[d]
    return data

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Original: ")
print(lst)
print("Custom Shuffle: ")
for _ in range(3):
    print(rand_shuffle(lst))

# Output
# Original: 
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Custom Shuffle:
# [4, 9, 7, 1, 3, 2, 5, 8, 6, 10]
# [9, 6, 1, 4, 10, 7, 8, 3, 5, 2]
# [10, 3, 1, 4, 8, 7, 6, 5, 2, 9]