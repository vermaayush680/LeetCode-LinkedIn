"""
Time Complexity: O(n)
Space Complexity: O(1)
"""

def check(self,n:int):
	a=0
	while(n>0):
		d=n%10
		a+=d**2
		n=n//10
	return a

def isHappy(self, n: int) -> bool:
	slow = n
	fast = self.check(n)
	while fast!=1 and fast!=slow:
		slow=self.check(slow)
		fast=self.check(self.check(fast))
	return fast==1
