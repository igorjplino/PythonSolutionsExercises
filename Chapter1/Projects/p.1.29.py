import itertools

def generate_permutations(chars):
    permutations = itertools.permutations(chars)
    permuted_strings = [''.join(p) for p in permutations]
    return list(permuted_strings)

def permute(chars):
    results = []
    def _permute(current, remaining):
        if not remaining:
            results.append(current)
        else:
            for i in range(len(remaining)):
                next_current = current + remaining[i]
                next_remaining = remaining[:i] + remaining[i+1:]
                _permute(next_current, next_remaining)
                
    _permute("", chars)
    return results

# chars = ["c", "a", "t", "d", "o", "g"]
chars = ["a", "b", "c"]

print(list(permute(chars)))
print(list(generate_permutations(chars)))

# Output
# ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
# ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

