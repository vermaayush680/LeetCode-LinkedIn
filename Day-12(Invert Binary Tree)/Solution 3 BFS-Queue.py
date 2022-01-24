def invertTree(self, root):
    stack = [root]
    while len(stack)>0:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left
            stack.append(node.right)
            stack.append(node.left)
    return root
