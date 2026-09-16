def _infer_embedded_object(value):
    if value is None:
        return False
    if isinstance(value, list):
        if not value:
            return False
        value = value[0]
    if isinstance(value, CIMInstance):
        return 'instance'
    if isinstance(value, CIMClass):
        return 'object'
    return False