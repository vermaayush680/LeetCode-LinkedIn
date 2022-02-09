"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
def addDigits(self,num):
    def check(n):
        a=0
        while(n>0):
                a+=n%10
                n//=10
        return a
    while num>9:
        num=check(num)
    return num


