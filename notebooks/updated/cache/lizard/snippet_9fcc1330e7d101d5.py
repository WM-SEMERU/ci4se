def _is_valid_collection_json(self, json_repr):
    collection = self._coerce_json_to_collection(json_repr)
    if collection is None:
        return False
    aa = validate_collection(collection)
    errors = aa[0]
    for e in errors:
        _LOG.debug('> invalid JSON: {m}'.format(m=e.encode('utf-8')))
    if len(errors) > 0:
        return False
    return True