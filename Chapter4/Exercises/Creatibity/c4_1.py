def find_max(s, index = 0):
    if index == len(s) - 1:
        return s[index]
    max_c = find_max(s, index + 1)
    return max(max_c, s[index])


print(find_max([-45,2,774,5,6,7,8]))
print(find_max([8,7,6,5,4,3,2,1]))