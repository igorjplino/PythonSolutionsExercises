lst = []

while True:
    try:
        lst.append(input())
    except EOFError:
        for l in range(len(lst), 0, -1):
            print(lst[l])