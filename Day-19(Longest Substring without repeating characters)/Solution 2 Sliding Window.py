"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
w=set()
q=collections.deque([])
m=0
for i in s:
    if i in w:
        while q:
            prev = q.popleft()
            w.remove(prev)
            if prev==i:
                break
    q.append(i)
    w.add(i)
    m=max(m,len(w))
return m
