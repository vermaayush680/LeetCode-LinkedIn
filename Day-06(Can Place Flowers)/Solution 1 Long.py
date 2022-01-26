"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
if n==0:
    return True
if len(f)==1:
    if f[0]==0 and n==1:
        return True
    else:
        return False

if f[0]==0 and f[1]==0:
    f[0]=1
    n-=1
if n==0:
    return True

i=1
while(n>0 and i<(len(f)-1)):
    if f[i]==0 and f[i-1]==0 and f[i+1]==0:
        f[i]=1
        n-=1
    i+=1

if f[len(f)-1]==0 and f[len(f)-2]==0 and n>0:
    f[n-1]=1
    n-=1

if n==0:
    return True
else:
    return False
