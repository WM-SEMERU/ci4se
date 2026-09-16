def updateFromKwargs(self, kwargs, properties, collector, **kw):
    yield self.collectChildProperties(kwargs=kwargs, properties=properties,
        collector=collector, **kw)
    if self.name:
        d = properties.setdefault(self.name, {})
    else:
        d = properties
    d.update(kwargs[self.fullName])