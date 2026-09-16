def compile_dependencies(self, sourcepath, include_self=False):
    items = self.inspector.parents(sourcepath)
    if include_self:
        items.add(sourcepath)
    return filter(None, [self.compile_source(item) for item in items])