"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
w=set()
c=0
m=0
for i in s:
    if i in w:
        m=max(m,c)
        c=0
        w=set(i)
    c+=1
    w.add(i)
m=max(m,c)
return m
