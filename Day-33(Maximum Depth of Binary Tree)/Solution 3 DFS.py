"""
Time Complexity: O(T)
Space Complexity: O(T)
"""
def maxDepth(self,root):
    ans = 0
    if not root:
        return 0
    stack = [] # stack
    stack.append((root,1))
    while DFS:
        root, depth = stack.pop()
        if depth > ans:
            ans = depth
        if root.left:
            stack.append((root.left, depth + 1))
        if root.right:
            stack.append((root.right, depth + 1))
    return ans

