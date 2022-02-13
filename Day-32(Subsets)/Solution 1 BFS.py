"""
Time Complexity: O(N * 2^N)
Space Complexity: O(N * 2^N)
"""
def subsets(self,nums):
    out=[[]]
    for i in nums:
        out+=[j+[i] for j in out]
    return out
