def as_objective(obj):
    if isinstance(obj, Objective):
        return obj
    elif callable(obj):
        return obj
    elif isinstance(obj, str):
        layer, n = obj.split(':')
        layer, n = layer.strip(), int(n)
        return channel(layer, n)