def aggregate(obj_a, obj_b, level=False, map_class=Map, sequence_class=Sequence
    ):
    deep, subdeep = levelise(level)
    if deep:
        obj_a = mark(obj_a, map_class=map_class, sequence_class=sequence_class)
        obj_b = mark(obj_b, map_class=map_class, sequence_class=sequence_class)
    if isinstance(obj_a, dict) and isinstance(obj_b, dict):
        if isinstance(obj_a, Aggregate) and isinstance(obj_b, Aggregate):
            response = copy.copy(obj_a)
        else:
            response = copy.copy(obj_b)
        for key, value in six.iteritems(obj_b):
            if key in obj_a:
                value = aggregate(obj_a[key], value, subdeep, map_class,
                    sequence_class)
            response[key] = value
        return response
    if isinstance(obj_a, Sequence) and isinstance(obj_b, Sequence):
        response = obj_a.__class__(obj_a[:])
        for value in obj_b:
            if value not in obj_a:
                response.append(value)
        return response
    response = copy.copy(obj_b)
    if isinstance(obj_a, Aggregate) or isinstance(obj_b, Aggregate):
        log.info('only one value marked as aggregate. keep `obj_b` value')
        return response
    log.debug('no value marked as aggregate. keep `obj_b` value')
    return response