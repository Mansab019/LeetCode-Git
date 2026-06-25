# brute Force method to solve the problem of returning the squares of a sorted array in non-decreasing order.


def sortedSquares(nums):
    squares = [x ** 2 for x in nums]
    squares.sort()
    return squares

 


# Two pointer Approach to solve the problem of returning the squares of a sorted array in non-decreasing order.

def sorted_squares_two_pointer(nums):
    left = 0
    right = len(nums) - 1
    result = [0] * len(nums)
    pos = len(nums) - 1
    
    while left <= right:
        left_sq = nums[left] ** 2
        right_sq = nums[right] ** 2
        if left_sq > right_sq:
            result[pos] = left_sq
            left +=1
        else:
            result[pos] = right_sq
            right -= 1
        pos -= 1
    return result
    
nums = [-4, -1, 0, 3, 10]
print(f"The brute Force method {sortedSquares(nums)}")
print(f"The two pointer method {sorted_squares_two_pointer(nums)}")