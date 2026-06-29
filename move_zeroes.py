# Problem: Move Zeroes
# Link: https://leetcode.com/problems/move-zeroes/
# File: move_zeroes.py


# -------------------------
# Approach 1: Brute Force
# Time: O(n) | Space: O(n)
# -------------------------
def moveZero_brute(nums):
    temp = []

    for num in nums:
        if num != 0:
            temp.append(num)

    nz = len(temp)

    for i in range(nz):
        nums[i] = temp[i]
    for i in range(nz, len(nums)):
        nums[i] = 0

    return nums


# -------------------------
# Approach 2: Two Pointer (Optimal)
# Time: O(n) | Space: O(1)
# -------------------------
def moveZero(nums):
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
    return nums


# -------------------------
# Test
# -------------------------
nums = [0, 1, 0, 3, 12]
print(moveZero(nums))  # Expected: [1, 3, 12, 0, 0]