def is_manager(self, path):
    node = self.get_node(path)
    if not node:
        return False
    return node.is_manager