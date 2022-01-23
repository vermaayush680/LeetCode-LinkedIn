"""
Time Complexity: O(n)
Space Complexity: O(1)
"""

c=0
can=0
for i in nums:
    if c==0:
        can = i
    if i==can:
        c+=1
    else:
        c-=1
return can
