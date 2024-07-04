def sumsquares(k):
    sum = 0
    if k <= 0:
        return sum    
    for i in range(1, k):
        sum += i * i
    return sum

print(sumsquares(10))
print(sumsquares(100))
print(sumsquares(50))

# Outputs:
# 285
# 328350
# 40425