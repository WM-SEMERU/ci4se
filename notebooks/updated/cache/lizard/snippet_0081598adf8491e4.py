def columns(self, dimensions=None):
    if dimensions is None:
        dimensions = self.dimensions()
    else:
        dimensions = [self.get_dimension(d, strict=True) for d in dimensions]
    return OrderedDict([(d.name, self.dimension_values(d)) for d in dimensions]
        )