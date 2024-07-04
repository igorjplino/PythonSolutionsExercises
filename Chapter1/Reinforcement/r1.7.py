def sum_odd_squares(k):
    return sum(i*i for i in range(1, k) if i % 2 == 1)


print(sum_odd_squares(10))
print(sum_odd_squares(100))
print(sum_odd_squares(50))
print(sum_odd_squares(713))

# Outputs:
# 165
# 166650
# 20825
# 60157236