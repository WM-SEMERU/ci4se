def _maybe_make_dimension(self, dimension):
    if isinstance(dimension, Dimension):
        return dimension
    if isinstance(dimension, units.UnitDescriptor):
        return Dimension.from_unit_descriptor(dimension)
    if isinstance(dimension, str):
        return Dimension.from_string(dimension)
    raise TypeError('Cannot convert %s to a dimension', dimension)