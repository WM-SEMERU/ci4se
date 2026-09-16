def fieldvalue_pairs(self, exclude_cache=False):
    for field in self._meta.scalarfields:
        if exclude_cache and field.as_cache:
            continue
        name = field.attname
        if hasattr(self, name):
            yield field, getattr(self, name)