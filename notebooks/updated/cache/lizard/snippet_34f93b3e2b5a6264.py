def retrieve(self, filter_expression=None, order_expression=None, slice_key
    =None):
    ents = iter(self.__entities)
    if not filter_expression is None:
        ents = filter_expression(ents)
    if not order_expression is None:
        ents = iter(order_expression(ents))
    if not slice_key is None:
        ents = islice(ents, slice_key.start, slice_key.stop)
    return ents