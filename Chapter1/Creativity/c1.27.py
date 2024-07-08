def factors(n):
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n:
        yield k

def sorted_factors(n):
    k = 1
    bigger_numebers = []
    while k * k < n:
        if n % k == 0:
            yield k
            bigger_numebers.append(n // k)
        k += 1
    if k * k == n:
        yield k
    for i in range(len(bigger_numebers) - 1, -1, -1):
        yield bigger_numebers[i]

def sorted_factors2(n):
    k = 1
    while k * k <= n:
        if n % k == 0:
            yield k
        k += 1
    
    k -= 1
    while k > 0:
        if n % k == 0 and n // k != k:
            yield n // k
        k -= 1

n = 100
print(list(factors(n)))
print(list(sorted_factors(n)))
print(list(sorted_factors2(n)))

# Outputs
# [1, 100, 2, 50, 4, 25, 5, 20, 10]
# [1, 2, 4, 5, 10, 20, 25, 50, 100]
# [1, 2, 4, 5, 10, 20, 25, 50, 100]