def subarraySum(self,nums,k):
    count = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if sum(nums[i:j+1]) == k:
                count += 1
    return count
