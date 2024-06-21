#Problem 3_5
height = list(map(int, input("Enter sequence of seats: ").split()))

def max_water(height):
    n = len(height)
    left, right = 0, n - 1
    left_max, right_max = 0, 0
    water = 0
    while left < right:
        if height[left] < height[right]:
            water += max(0, left_max - height[left])
            left_max = max(left_max, height[left])
            left += 1
        else:  
            water += max(0, right_max - height[right])  
            right_max = max(right_max, height[right])
            right -= 1
    return water

water = max_water(height)
print("Water:", water)