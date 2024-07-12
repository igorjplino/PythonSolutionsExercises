import random

def random_upper_case(sentence):
    i = random.randint(0, len(sentence)) - 1
    return sentence[:i] + sentence[i].upper() + sentence[i+1:] + f" <- Upper at index {i}"

amount_times = 100
sentence = "I will never spam my friends again."

random_sentence = random.sample(range(amount_times), 8)

for i in range(amount_times):
    s = sentence
    if i in random_sentence:
        s = random_upper_case(s)

    print(f"{i+1}. {s}")

