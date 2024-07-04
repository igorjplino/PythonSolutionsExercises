def is_all_different(lst):
    numbers = set()
    for i in lst:
        if i in numbers:
            return False
        numbers.add(i)
    return True

print(is_all_different([1, 2, 3, 4, 5]))
print(is_all_different([1, 2, 3, 4, 1]))

# Outputs
# True
# False