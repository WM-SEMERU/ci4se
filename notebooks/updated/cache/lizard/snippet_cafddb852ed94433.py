def canonical_value(self, query):
    for d in self.descriptors:
        if query in d:
            return d.canonical_label
    return None