def query(cls, expression=None, order_by=None):
    if expression is not None:
        executor = Executor(cls.__database__)
        result = executor.execute(expression)
    else:
        result = cls._query.all_index()
    if order_by is not None:
        desc = False
        if isinstance(order_by, Desc):
            desc = True
            order_by = order_by.node
        alpha = not isinstance(order_by, _ScalarField)
        result = cls.__database__.sort(result.key, by='*->%s' % order_by.
            name, alpha=alpha, desc=desc)
    elif isinstance(result, ZSet):
        result = result.iterator(reverse=True)
    for hash_id in result:
        yield cls.load(hash_id, convert_key=False)