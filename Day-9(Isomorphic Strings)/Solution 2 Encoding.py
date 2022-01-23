"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
def isIsomorphic(self, s: str, t: str) -> bool:
  return self.encoding(s)==self.encoding(t)  

def encoding(self,s):
  d={}
  encoded=[]
  for c in s:
      if c not in d:
          d[c]=len(d)
      encoded+=[d[c]]
  return encoded

  return True
