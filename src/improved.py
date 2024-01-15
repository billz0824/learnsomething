def max_area(height):
    max_area = 0
    i = 0
    n = len(height) - 1
    while n > i:
        max_area = max(max_area, (n - i) * min(height[n], height[i]))
        if height[i] <= height[n]:
            i += 1
        else:
            n -= 1
    return max_area
