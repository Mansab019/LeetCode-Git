# Problem: Max Consecutive Ones
# Link: https://leetcode.com/problems/max-consecutive-ones/
# File: max_consecutive_ones.py


# -------------------------
# Approach 1: Simple Counter (Optimal)
# Time: O(n) | Space: O(1)
# -------------------------
def findMaxConsecutiveOnes(nums):
    count = 0
    max_count = 0

    for num in nums:
        if num == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0

    return max_count


# -------------------------
# Approach 2: Ternary Expression
# Time: O(n) | Space: O(1)
# -------------------------
def findMaxConsecutiveOnes_ternary(nums):
    count = 0
    max_count = 0

    for num in nums:
        count = count + 1 if num == 1 else 0
        max_count = max(max_count, count)

    return max_count


# -------------------------
# Approach 3: Split Trick (Pythonic)
# Time: O(n) | Space: O(n)
# -------------------------
def findMaxConsecutiveOnes_split(nums):
    return max(
        len(group)
        for group in ''.join(map(str, nums)).split('0')
    )


# -------------------------
# Test
# -------------------------
nums = [1, 1, 0, 1, 1, 1]
print(findMaxConsecutiveOnes(nums))          # Expected: 3
print(findMaxConsecutiveOnes_ternary(nums))  # Expected: 3
print(findMaxConsecutiveOnes_split(nums))    # Expected: 3