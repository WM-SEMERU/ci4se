def _get_obj_attr(cls, obj, path, pos):
    field = path[pos]
    if isinstance(obj, (dict, Mapping)):
        return obj[field], pos
    elif isinstance(obj, (list, Sequence)):
        join_operation = cls.SEQUENCE_OPERATIONS.get(field)
        if join_operation is not None:
            return AnySequenceResult(cls._sequence_map(obj, path[pos + 1:]),
                join_operation), len(path) + 1
        else:
            return obj[int(field)], pos
    else:
        return getattr(obj, field, None), pos