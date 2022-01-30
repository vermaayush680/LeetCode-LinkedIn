"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[]
        pref=[0]*(n+1)
        for i in range(n):
            pref[i+1]=pref[i]+nums[i]
        zero,total,one=0,0,0
        m=-1
        for i in range(n+1):
            one=pref[n]-pref[i]
            zero=i-pref[i]
            total=zero+one
            if total>m:
                m=total
                res=[]
            if total==m:
                res+=[i]
        return res
