"""
Time Complexity: O(T)
Space Complexity: O(1)
"""
def maxDepth(self,root):
    def dfs(root, depth):
        if not root: return depth
        return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
    return dfs(root, 0)

