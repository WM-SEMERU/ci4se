def produce(cls, mapped_props, aggregated, value_type, visitor):
    kwargs = {} if not mapped_props else dict((k.name, v) for k, v in
        mapped_props)
    if issubclass(value_type, Collection):
        kwargs['values'] = aggregated
    return value_type(**kwargs)