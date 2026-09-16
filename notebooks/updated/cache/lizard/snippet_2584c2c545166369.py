def drop_dimension(self, dimensions):
    dimensions = [dimensions] if np.isscalar(dimensions) else dimensions
    dims = [d for d in self.kdims if d not in dimensions]
    dim_inds = [self.get_dimension_index(d) for d in dims]
    key_getter = itemgetter(*dim_inds)
    return self.clone([(key_getter(k), v) for k, v in self.data.items()],
        kdims=dims)