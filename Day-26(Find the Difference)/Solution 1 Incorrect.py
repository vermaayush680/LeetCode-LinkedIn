"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
def findTheDifference(self,s,t):
    d=set()
    n=len(s)
    for i in range(n):
        if s[i] not in d:
                d.add(s[i])
    for i in t:
        if i not in d:
                return i
