def group_join(self, inner_enumerable, outer_key=lambda x: x, inner_key=lambda
    x: x, result_func=lambda x: x):
    if not isinstance(inner_enumerable, Enumerable):
        raise TypeError(
            'inner enumerable parameter must be an instance of Enumerable')
    return Enumerable(itertools.product(self, inner_enumerable.
        default_if_empty())).group_by(key_names=['id'], key=lambda x:
        outer_key(x[0]), result_func=lambda g: (g.first()[0], g.where(lambda
        x: inner_key(x[1]) == g.key.id).select(lambda x: x[1]))).select(
        result_func)