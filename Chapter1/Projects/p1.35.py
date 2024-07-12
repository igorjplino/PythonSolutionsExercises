import random

def generate_birthdays(amount_people):
    return [random.randint(1, 365) for _ in range(amount_people)]

def has_duplicate(birthdays):
    return len(birthdays) != len(set(birthdays))

def simulate_birthdays(n, trials):
    shared_birthdays = 0
    for _ in range(trials):
        birthdays = generate_birthdays(n)
        if has_duplicate(birthdays):
            shared_birthdays += 1
    return (shared_birthdays / trials) * 100

trials = 10000
for n in range(5, 105, 5):
    probability = simulate_birthdays(n, trials)
    print(f"{n:3} | {probability:.2f}%")

# Output
#   5 | 2.40%
#  10 | 10.70%
#  15 | 23.80%
#  20 | 40.90%
#  25 | 58.50%
#  30 | 70.60%
#  35 | 81.80%
#  40 | 89.20%
#  45 | 94.80%
#  50 | 97.50%
#  55 | 98.60%
#  60 | 99.00%
#  65 | 99.90%
#  70 | 100.00%
#  75 | 99.90%
#  80 | 100.00%
#  85 | 100.00%
#  90 | 100.00%
#  95 | 100.00%
# 100 | 100.00%