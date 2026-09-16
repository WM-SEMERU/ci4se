def children(self):
    if self.left and self.left.data is not None:
        yield self.left, 0
    if self.right and self.right.data is not None:
        yield self.right, 1