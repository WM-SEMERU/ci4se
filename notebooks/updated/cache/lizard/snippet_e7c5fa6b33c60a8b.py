def get_all_parent_edges(self):
    all_parent_edges = set()
    for parent in self.parents:
        all_parent_edges.add((self.item_id, parent.item_id))
        all_parent_edges |= parent.get_all_parent_edges()
    return all_parent_edges