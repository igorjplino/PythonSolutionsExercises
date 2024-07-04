def check_distinct_odd(lst):
    odd_numbers = set()
    for l in lst:
        if l % 2 != 0:
            odd_numbers.add(l)
            if len(odd_numbers) > 1:
                return True
    return False

print(check_distinct_odd([1, 2, 3, 4, 5]))
print(check_distinct_odd([1, 2, 4, 6, 8, 10]))
print(check_distinct_odd([1, 2, 4, 6, 10, 15]))

# Output
# True
# False
# True