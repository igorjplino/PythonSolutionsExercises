import random

def random_choice(data):
    return data[random.randrange(0, len(data))]

s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(random_choice(s), end = " ")