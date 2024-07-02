def sumsquares1(k):
    sum = 0
    if k <= 0:
        return sum    
    for i in range(1, k):
        sum += i * i
    return sum

def sumsquares2(k):
    if k <= 0:
        return 0    
    return sum(i*i for i in range(1, k))

print(sumsquares1(10))
print(sumsquares2(10))

print(sumsquares1(100))
print(sumsquares2(100))

print(sumsquares1(50))
print(sumsquares2(50))