def runningSum(nums):
    """
    Given an array nums, return the running sum of nums.
    
    The running sum of an array is defined as runningSum[i] = sum(nums[0]…nums[i]).
    
    :param nums: List[int] - The input array of integers.
    :return: List[int] - The running sum of the input array.
    """
    running_sum = []
    current_sum = 0
    
    for num in nums:
        current_sum += num
        running_sum.append(current_sum)
    
    return running_sum

nums = [1, 2, 3, 4]
print(runningSum(nums))  # Expected: [1, 3, 6, 10]