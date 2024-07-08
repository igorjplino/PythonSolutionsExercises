
def array_insert(lst, index, value):
    print("original list: ")
    print(lst)
    try:
        lst[index] = value
        print("Updated list: ")
        print(lst)
    except IndexError:
        print("Don’t try buffer overflow attacks in Python!")
    print()
    return lst

array_insert([1, 2, 3], 4, 5)
array_insert([1, 2, 3, 4, 5], 4, 10)
array_insert([1, 2, 3], 1, "Hello")

# Output
# original list: 
# [1, 2, 3]
# Don’t try buffer overflow attacks in Python!

# original list:
# [1, 2, 3, 4, 5]
# Updated list:
# [1, 2, 3, 4, 10]
 
# original list:
# [1, 2, 3]
# Updated list:
# [1, 'Hello', 3]