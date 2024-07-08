def count_vowels(lst):
    vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
    count = 0
    for l in lst:
         if l in vowels:
              count += 1
    return count

print(count_vowels("hello"))
print(count_vowels("abcdefghijklmnopqrstuvwxyz"))
print(count_vowels("gOod bye"))
