def divider_by_2(n):
    if n <= 2:
        raise ValueError("The value must be higher than 2")

    count = 0
    while n >= 2:
        n /= 2
        count += 1
    return count

print(divider_by_2(10))
print(divider_by_2(15))
print(divider_by_2(33))
print(divider_by_2(75))
print(divider_by_2(111))

# Output
# 3
# 3
# 5
# 6
# 6