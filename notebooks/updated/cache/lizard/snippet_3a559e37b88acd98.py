def _append_node(self, child):
    self.body.append(child)
    child.parent = self