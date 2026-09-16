def delete_annotations(event, key, namespace=None, matchfunc=None):
    if matchfunc is None:
        matchfunc = _is_equal
    if isinstance(key, Exception):
        key = _error_repr(key)
    newanns = [ann for ann in event.get('_humilis', {}).get('annotation', [
        ]) if not (matchfunc(key, ann['key']) and (namespace is None or ann
        .get('namespace') == namespace))]
    replace_event_annotations(event, newanns)