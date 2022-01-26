"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
c=0
f=[0]+f+[0]
for i in range(1,len(f)-1):
    if f[i-1]==f[i]==f[i+1]==0:
        c+=1
        f[i]=1
return c>=n
