def prune_unrepresented(self):
    for node in self.depth_first_iter(self_first=False):
        if not node.children and not node.sequence_ids and node is not self:
            node.parent.remove_child(node)