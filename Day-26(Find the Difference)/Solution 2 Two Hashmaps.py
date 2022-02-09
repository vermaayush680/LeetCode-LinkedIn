"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
def findTheDifference(self,s,t):
    d1={}
    d2={}
    n=len(t)
    for i in range(n):
        if i<n-1:
            if s[i] not in d1:
                d1[s[i]]=1
            else:
                d1[s[i]]+=1
        if t[i] not in d2:
            d2[t[i]]=1
        else:
            d2[t[i]]+=1  
    for i in d2:
        if (i not in d1) or (d1[i]!=d2[i]):
            return i
