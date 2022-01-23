"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
if not root:
    return True
queue=[root.left,root.right]

while(len(queue)>0):
    left=queue.pop(0)
    right=queue.pop(0)

    if not left and not right:
        continue
    elif left and right and left.val==right.val:
        pass
    else:
        return False

    queue.append(left.left)
    queue.append(right.right)
    queue.append(left.right)
    queue.append(right.left)
return True
