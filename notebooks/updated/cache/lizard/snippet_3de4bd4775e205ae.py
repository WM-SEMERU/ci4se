def label(self):
    if self.valuetype_class.is_label():
        return self
    for c in self.table.columns:
        if c.parent == self.name and c.valuetype_class.is_label():
            return c
    return None