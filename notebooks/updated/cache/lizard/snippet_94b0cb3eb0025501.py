def tree_has_single_path(self, node):
    num_children = len(node.children)
    if num_children > 1:
        return False
    elif num_children == 0:
        return True
    else:
        return True and self.tree_has_single_path(node.children[0])