"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
for i in range(len(nums)):
    if target==nums[i]:
        return i
return -1
