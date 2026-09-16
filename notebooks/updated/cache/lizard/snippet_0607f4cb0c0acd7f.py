def _initialize_splittable_and_unsplittable_dims(self,
    default_splittability, exception_dims_iterable=None):
    default_dims = set()
    exception_dims = set()
    if exception_dims_iterable:
        exception_dims.update(exception_dims_iterable)
    for t in itertools.chain(self.inputs, self.outputs):
        for dim_name in t.shape.dimension_names:
            if dim_name not in exception_dims:
                default_dims.add(dim_name)
    if default_splittability == 'splittable':
        return frozenset(default_dims), frozenset(exception_dims)
    elif default_splittability == 'unsplittable':
        return frozenset(exception_dims), frozenset(default_dims)
    else:
        raise ValueError(
            'default_splittability should be either "splittable" or "unsplittable" but was {}'
            .format(default_splittability))