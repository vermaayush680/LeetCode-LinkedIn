def invertTree1(self, root):
  if root:
      root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
      return root
