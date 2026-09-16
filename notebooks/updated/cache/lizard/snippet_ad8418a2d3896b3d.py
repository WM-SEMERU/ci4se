def has_method(obj, name):
    if obj == None:
        raise Exception('Object cannot be null')
    if name == None:
        raise Exception('Method name cannot be null')
    name = name.lower()
    for method_name in dir(obj):
        if method_name.lower() != name:
            continue
        method = getattr(obj, method_name)
        if MethodReflector._is_method(method, method_name):
            return True
    return False