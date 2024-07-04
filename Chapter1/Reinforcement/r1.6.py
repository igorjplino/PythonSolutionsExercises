def sum_odd_squares(k):  
    sum = 0
    if k <= 0:
        return sum    
    for i in range(1, k):
        if i % 2 == 1:
            sum += i * i
    return sum


print(sum_odd_squares(10))
print(sum_odd_squares(100))
print(sum_odd_squares(50))
print(sum_odd_squares(713))

# Outputs:
# 165
# 166650
# 20825
# 60157236