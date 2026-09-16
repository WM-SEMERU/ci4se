def register(self, source, attributes=None, allow_class=False,
    allow_subclasses=True, propagate_attributes=True, inherit_attributes=True):
    if source in self.sources:
        raise AlreadyRegistered(self, source)
    parent_sources = set()
    if inherit_attributes:
        bases = source.__bases__ if isinstance(source, type
            ) else source.__class__.__bases__
        for klass in bases:
            if klass in self.sources and self.sources[klass
                ].propagate_attributes:
                parent_sources.add(self.sources[klass])
    self.sources[source] = self.Source(source, attributes, allow_class,
        allow_subclasses, propagate_attributes, inherit_attributes,
        parent_sources)
    if propagate_attributes:
        for src in self.sources.values():
            if src.source != source and src.inherit_attributes and issubclass(
                src.source, source):
                src.parent_source.add(self.sources[source])