def invertTree2(self, root):
  queue = [root]
  while len(queue)>0:
      node = queue.pop()
      if node:
          node.left, node.right = node.right, node.left
          queue.append(node.left)
          queue.append(node.right)
  return root
