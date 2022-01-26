"""
Time Complexity: O(n)
Space Complexity: O(1)
"""

last=-1
res=0
n=len(seats)
for i in range(n):
    if seats[i]:
        if last<0:
            res=max(res,i)
        else:
            res = max(res,(i-last)//2)
        last=i
return max(res,n-1-last)
