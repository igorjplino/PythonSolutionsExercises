def concat_dot(a, b):
    if (len(a) != len(b)):
        raise ValueError("Arrays must be of the same lenght")

    c = [0] * len(a)
    for i in range(len(a)):
        c[i] = a[i] * b[i]
    return c

print(concat_dot([1, 2, 3], [1, 2, 3]))
print(concat_dot([3, 2, 1], [1, 2, 3]))
print(concat_dot([5, 6, 7, 8, 9, 10], [0, 1, 2, 3, 4, 5]))
    
# Outputs:
# [1, 4, 9]
# [3, 4, 3]
# [0, 6, 14, 24, 36, 50]