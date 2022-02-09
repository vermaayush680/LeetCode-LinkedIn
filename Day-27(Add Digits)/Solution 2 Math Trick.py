"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
def addDigits(self,num):
    if num==0:
        return 0
    if num%9==0:
        return 9
    return num%9

