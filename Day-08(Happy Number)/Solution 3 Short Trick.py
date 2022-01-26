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
	while(n!=1) and n!=4:
		n=self.check(n)
		print(n)
	return n==1
