def minmax(data):
    min, max = data[0], data[0]
    for d in data[1:]:
        if d < min:
            min = d
        if d > max:
            max = d
    return min, max


print(minmax([21, 10, 43, 50, 32]))