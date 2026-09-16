def rename_nodes(self, renaming_map):
    if not isinstance(renaming_map, dict):
        raise TypeError('renaming_map must be a dict')
    for node in self.traverse_preorder():
        if node.label in renaming_map:
            node.label = renaming_map[node.label]