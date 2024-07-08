import string

def remove_punctuation(s):
    return "".join([c for c in s if c not in string.punctuation])

print(remove_punctuation("Let's try, Mike."))
print(remove_punctuation("Hello, world!"))

# Output
# Lets try Mike
# Hello world