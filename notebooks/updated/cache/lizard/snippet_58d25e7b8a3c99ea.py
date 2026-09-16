def _IN(self, value):
    if not self._indexed:
        raise datastore_errors.BadFilterError(
            'Cannot query for unindexed property %s' % self._name)
    from .query import FilterNode
    if not isinstance(value, (list, tuple, set, frozenset)):
        raise datastore_errors.BadArgumentError(
            'Expected list, tuple or set, got %r' % (value,))
    values = []
    for val in value:
        if val is not None:
            val = self._do_validate(val)
            val = self._call_to_base_type(val)
            val = self._datastore_type(val)
        values.append(val)
    return FilterNode(self._name, 'in', values)