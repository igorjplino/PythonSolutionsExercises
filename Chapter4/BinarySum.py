def binary_sum(s, start, stop):
    """
    When a function makes two recursive calls, we say that it uses binary recursion.
    """
    if start >= stop:
        return 0
    elif start == stop - 1:
        return s[start]
    
    mid = (start + stop) // 2

    return binary_sum(s, start, mid) + binary_sum(s, mid, stop)

if __name__ == "__main__":
    s = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
    start = 0
    stop = len(s)
    result = binary_sum(s, start, stop)

    print(result)
