def get_annotations(event, key, namespace=None, matchfunc=None):
    if matchfunc is None:
        matchfunc = _is_equal
    if isinstance(key, Exception):
        key = _error_repr(key)
    return [ann for ann in event.get('_humilis', {}).get('annotation', []) if
        matchfunc(key, ann['key']) and (namespace is None or ann.get(
        'namespace') == namespace)]