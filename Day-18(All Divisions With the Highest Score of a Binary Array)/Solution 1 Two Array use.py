"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n=len(nums)
        zero=[0]*(n+1)
        one=[0]*(n+1)
        for i in range(n):
            zero[i+1]=zero[i]+(nums[i]==0)
        for i in range(n-1,-1,-1):
            one[i]=one[i+1]+(nums[i]==1)
        total = [0]*(n+1)
        m=0
        res=[]
        for i in range(n+1):
            total[i]=zero[i]+one[i]
            if total[i]>m:
                res=[]
                m=total[i]
            if total[i]==m:
                res+=[i]
        return res
