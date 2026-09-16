def is_compatible(self, other):
    if isinstance(other, type(self)):
        try:
            if not self.dx == other.dx:
                raise ValueError('%s sample sizes do not match: %s vs %s.' %
                    (type(self).__name__, self.dx, other.dx))
        except AttributeError:
            raise ValueError(
                'Series with irregular xindexes cannot be compatible')
        if not self.unit == other.unit and not (self.unit in [
            dimensionless_unscaled, None] and other.unit in [
            dimensionless_unscaled, None]):
            raise ValueError('%s units do not match: %s vs %s.' % (type(
                self).__name__, str(self.unit), str(other.unit)))
    else:
        arr = numpy.asarray(other)
        if arr.ndim != self.ndim:
            raise ValueError('Dimensionality does not match')
        if arr.dtype != self.dtype:
            warn('Array data types do not match: %s vs %s' % (self.dtype,
                other.dtype))
    return True