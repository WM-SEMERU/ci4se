def _iter_errors_custom(instance, checks, options):
    for v_function in checks:
        try:
            result = v_function(instance)
        except TypeError:
            result = v_function(instance, options)
        if isinstance(result, Iterable):
            for x in result:
                yield x
        elif result is not None:
            yield result
    for field in instance:
        if type(instance[field]) is list:
            for obj in instance[field]:
                if _is_stix_obj(obj):
                    for err in _iter_errors_custom(obj, checks, options):
                        yield err