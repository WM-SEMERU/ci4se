def _categorize_data(self, data, cols, dims):
    if self.invert_axes:
        cols = cols[::-1]
        dims = dims[:2][::-1]
    ranges = [self.handles['%s_range' % ax] for ax in 'xy']
    for i, col in enumerate(cols):
        column = data[col]
        if isinstance(ranges[i], FactorRange) and (isinstance(column, list) or
            column.dtype.kind not in 'SU'):
            data[col] = [dims[i].pprint_value(v) for v in column]