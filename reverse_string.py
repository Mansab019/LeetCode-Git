# Problem: Reverse String
# Link: https://leetcode.com/problems/reverse-string/
# File: reverse_string.py


# -------------------------
# Approach 1: Built-in Reverse (Brute Force)
# Time: O(n) | Space: O(1) (in-place, but relies on built-in)
# -------------------------
def reverseString_builtin(s):
    s.reverse()
    return s


# -------------------------
# Approach 2: Two Pointer (Optimal)
# Time: O(n) | Space: O(1)
# -------------------------
def reverseString(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s


# -------------------------
# Test
# -------------------------
s1 = ["h", "e", "l", "l", "o"]
s2 = ["h", "e", "l", "l", "o"]

print(reverseString_builtin(s1))  # Expected: ['o','l','l','e','h']
print(reverseString(s2))          # Expected: ['o','l','l','e','h']