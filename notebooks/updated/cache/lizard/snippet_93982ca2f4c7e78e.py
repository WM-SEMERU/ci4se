def get_parent_label(self, treepos):
    parent_pos = self.get_parent_treepos(treepos)
    if parent_pos is not None:
        parent = self.dgtree[parent_pos]
        return parent.label()
    else:
        return None