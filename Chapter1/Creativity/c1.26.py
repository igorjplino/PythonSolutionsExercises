def is_correct_arithmetic(a, b, c):
    if a + b == c:
        return True
    if a == b - c:
        return True
    if a * b == c:
        return True
    return False

print(is_correct_arithmetic(1, 2, 3))
print(is_correct_arithmetic(5, 8, 3))
print(is_correct_arithmetic(2, 3, 6))
print(is_correct_arithmetic(1, 1, 3))

# Output
# True
# True
# True
# False