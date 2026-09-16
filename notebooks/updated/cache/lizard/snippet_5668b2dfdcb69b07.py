def compute_depth(self):
    left_depth = self.left_node.compute_depth() if self.left_node else 0
    right_depth = self.right_node.compute_depth() if self.right_node else 0
    return 1 + max(left_depth, right_depth)