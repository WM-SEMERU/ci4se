def _extract_key_value(obj):
    key = None
    value = None
    if isinstance(obj, Value):
        key = _construct_new_key(obj.name, obj.units)
        value = []
        if obj.scalars:
            value = [(val.value if isinstance(val, Scalar) else val) for
                val in obj.scalars]
        elif obj.vectors and len(obj.vectors) == 1:
            value = [(val.value if isinstance(val, Scalar) else val) for
                val in obj.vectors[0]]
        if len(value) == 1:
            value = value[0]
        elif len(value) == 0:
            value = None
    if isinstance(obj, ProcessStep):
        key = 'Processing'
        value = obj.name
    return key, value