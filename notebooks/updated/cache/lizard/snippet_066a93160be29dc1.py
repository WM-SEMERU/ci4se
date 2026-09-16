def reindex(self, indexers=None, method=None, tolerance=None, copy=True, **
    indexers_kwargs):
    indexers = utils.either_dict_or_kwargs(indexers, indexers_kwargs, 'reindex'
        )
    bad_dims = [d for d in indexers if d not in self.dims]
    if bad_dims:
        raise ValueError('invalid reindex dimensions: %s' % bad_dims)
    variables, indexes = alignment.reindex_variables(self.variables, self.
        sizes, self.indexes, indexers, method, tolerance, copy=copy)
    coord_names = set(self._coord_names)
    coord_names.update(indexers)
    return self._replace_with_new_dims(variables, coord_names, indexes=indexes)