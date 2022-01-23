"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
b={}
for i in range(len(nums)):
  adder = target - nums[i]
  if adder in b:
    return [b[adder],i]
  else:
    b[nums[i]] = i
