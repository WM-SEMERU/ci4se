def update_heights(self, recursive=True):
    if self.node:
        if recursive:
            if self.node.left:
                self.node.left.update_heights()
            if self.node.right:
                self.node.right.update_heights()
        self.height = 1 + max(self.node.left.height, self.node.right.height)
    else:
        self.height = -1