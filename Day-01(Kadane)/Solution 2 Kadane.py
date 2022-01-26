"""
Kadane Solution
Time Complexity : O(n)
Space Complexity : O(1)
"""

n=len(prices)
maxSoFar=0
maxCur=0
for i in range(1,n):
    maxCur+=prices[i]-prices[i-1]
    maxCur=max(0,maxCur)
    maxSoFar=max(maxSoFar,maxCur)
return maxSoFar
