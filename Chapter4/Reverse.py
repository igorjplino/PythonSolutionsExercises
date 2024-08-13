def reverse(s, start, stop):
    if start < stop - 1:
        s[start], s[stop-1] = s[stop-1], s[start]
        reverse(s, start + 1, stop - 1)

def reverse_iterative(s):
    start, stop = 0, len(s)
    while start < stop - 1:
        s[start], s[stop-1] = s[stop-1], s[start]
        start += 1
        stop -= 1

if __name__ == "__main__":
    s = [4, 3, 6, 2, 8, 9, 5]
    start = 0
    stop = len(s)

    print(f"Original: {s}")
    reverse(s, start, stop)
    print(f"Reversed: {s}")
    print()
    print(f"Original: {s}")
    reverse_iterative(s)
    print(f"Reversed: {s}")


