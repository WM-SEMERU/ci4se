def add_to_fields(self):
    meta = self.model._meta
    meta.scalarfields.append(self)
    if self.index:
        meta.indices.append(self)