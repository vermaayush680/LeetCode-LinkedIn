"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
def findTheDifference(self,s,t):
    n=len(s)
    c=0
    for i in s:
        c^=ord(i)

    for i in t:
        c^=ord(i)

    return chr(c)
