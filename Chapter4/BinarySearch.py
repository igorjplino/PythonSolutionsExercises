def binary_search(data, target, low, high):
    """
    Return True if target is found in indicated portion of a Python list.
    The search only considers the portion from data[low] to data[high] inclusive.
    """

    if low > high:
        return False
    
    mid = (low + high) // 2
    if target == data[mid]:
        return True
    
    if target < data[mid]:
        return binary_search(data, target, low, mid - 1)

    return binary_search(data, target, mid + 1, high)

def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2

        if target == data[mid]:
            return True
        
        if target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    
    return False

if __name__ == "__main__":
    data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
    target = 22
    low = 0
    high = len(data) - 1
    
    result = binary_search(data, target, low, high)
    print(result)

    result = binary_search_iterative(data, target)
    print(result)