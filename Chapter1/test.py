from typing import List


def test1():
    lst = [1, 2, 3, 4, 5]
    i = 0
    next = lst[:i]
    end = lst[i + 1:]
    t = next + end

    print(next)
    print(end)
    print(t)

def test2():
    s = "I will never spam my friends again."
    print(s[34])

def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:
            currentArea = min(height[left], height[right]) * (right - left)
            maxArea = max(maxArea, currentArea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea

test2()