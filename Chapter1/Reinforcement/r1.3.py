def minmax(data):
    min, max = data[0], data[0]
    for d in data[1:]:
        if d < min:
            min = d
        if d > max:
            max = d
    return min, max


print(minmax([21, 10, 43, 50, 32]))
print(minmax([66, 10, 31, 78, 131]))
print(minmax([111, 321, 907, 64, 20]))

# Outputs
# (10, 50)
# (10, 131)
# (20, 907)