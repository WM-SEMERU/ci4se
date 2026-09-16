def children(self):
    for c in self.table.columns:
        if c.parent == self.name and not c.valuetype_class.is_label():
            yield c