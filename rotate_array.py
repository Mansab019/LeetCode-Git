def rotate (nums, k):
    n = len(nums)
    k = k % n
    
    def reverse(left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left +=1
            right -=1
            
    reverse(n-k, n-1)
    reverse(0, n-k-1)
    reverse(0, n-1)
        
nums = [1,2,3,4,5,6,7]
rotate(nums, 3)
print(nums)