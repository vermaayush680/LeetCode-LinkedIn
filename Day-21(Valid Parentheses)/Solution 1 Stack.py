"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
stack=[]
d={'}':'{',')':'(',']':'['}
for i in s:
    if i in d:
        if not stack:
            return False
        a=stack.pop()
        if d[i]!=a:
            return False
    else:
        stack.append(i)
if stack:
    return False
return True
