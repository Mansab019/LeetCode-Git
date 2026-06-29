# Problem: Shuffle the Array
# Link: https://leetcode.com/problems/shuffle-the-array/
# File: shuffle_the_array.py


# -------------------------
# Approach 1: Brute Force (Two Pointer)
# Time: O(n) | Space: O(n)
# -------------------------
def shuffle_brute(nums, n):
    result = []
    i = 0
    j = n

    while i < n:
        result.append(nums[i])
        result.append(nums[j])
        i += 1
        j += 1

    return result


# -------------------------
# Approach 2: Index Loop (Optimal Readable)
# Time: O(n) | Space: O(n)
# -------------------------
def shuffle(nums, n):
    result = []
    for i in range(n):
        result.append(nums[i])
        result.append(nums[i + n])
    return result


# -------------------------
# Approach 3: Zip (Most Pythonic)
# Time: O(n) | Space: O(n)
# -------------------------
def shuffle_zip(nums, n):
    result = []
    for x, y in zip(nums[:n], nums[n:]):
        result.append(x)
        result.append(y)
    return result


# -------------------------
# Test
# -------------------------
nums = [2, 5, 1, 3, 4, 7]
print(shuffle_brute(nums, 3))  # Expected: [2, 3, 5, 4, 1, 7]
print(shuffle(nums, 3))        # Expected: [2, 3, 5, 4, 1, 7]
print(shuffle_zip(nums, 3))    # Expected: [2, 3, 5, 4, 1, 7]