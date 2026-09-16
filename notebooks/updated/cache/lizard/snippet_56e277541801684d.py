def searchable_object_types(self):
    try:
        idx = self.index()
    except KeyError:
        return []
    with idx.reader() as r:
        indexed = sorted(set(r.field_terms('object_type')))
    app_indexed = self.app_state.indexed_fqcn
    return [(name, friendly_fqcn(name)) for name in indexed if name in
        app_indexed]