def find_min_max(s, index=0):
    if index == len(s) - 1: # test for base case
        return s[index], s[index] # returning the lastest values
    
    min_c, max_c = find_min_max(s, index+1)
    return min(s[index], min_c), max(s[index], max_c)
    
    
print(find_min_max([1,2,3,4,5]))
"""
# Recursion trace
5, 5 = find_min_max(s, 5) # reached the last position of the sequence, so 5 is bigger or equal to len(s)
4, 5 = find_min_max(s, 4) # start to evaluate the next values, 4 is less than 5
3, 5 = find_min_max(s, 3)
2, 5 = find_min_max(s, 2)
1, 5 = find_min_max(s, 1)
"""


print(find_min_max([-45,2,774,5,6,7,8]))
print(find_min_max([8,7,6,5,4,3,2,1]))