"""
Time Complexity: O(T)
Space Complexity: O(T)
"""
def maxDepth(self, root: Optional[TreeNode]) -> int:
    depth = 0
    level = [root] if root else []
    while level:
        depth += 1
        queue = []
        for i in level:
            if i.left:
                queue.append(i.left)
            if i.right:
                queue.append(i.right)
        level = queue
    return depth

