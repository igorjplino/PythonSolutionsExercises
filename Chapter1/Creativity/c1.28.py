def p_norm(v, p = 2):
    sum = 0
    for n in v:
        sum += n ** p
    return sum ** (1 / p)

def p_norm2(v, p = 2):
    return sum(n ** p for n in v) ** (1 / p)

print(p_norm((4, 3)))
print(p_norm2((4, 3)))
print(p_norm((4, 3), p = 3))
print(p_norm2((4, 3, 7, 8), p = 4))

# Output
# 5.0
# 5.0
# 4.497941445275415
# 9.092195045299102