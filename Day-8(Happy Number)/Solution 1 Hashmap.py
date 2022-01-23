"""
Time Complexity: O(n)
Space Complexity: O(n)
"""

def check(self,n:int):
	a=0
	while(n>0):
		d=n%10
		a+=d**2
		n=n//10
	return a

def isHappy(self, n: int) -> bool:
	d={n}
	while(n!=1):
		n=self.check(n)
		if n in d:
			return False
		d.add(n)
	return True
