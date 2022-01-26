"""
Brute Force Solution
Time Complexity : O(n^2)
Space Complexity : O(1)
"""

c=0
n=len(prices)
for i in range(n-1):
    for j in range(i+1,n):
        c=max(c,prices[j]-prices[i])
return c
