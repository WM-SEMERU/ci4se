def _convert_to_indexer(self, obj, axis=None, is_setter=False):
    if axis is None:
        axis = self.axis or 0
    if isinstance(obj, slice):
        return self._convert_slice_indexer(obj, axis)
    elif is_float(obj):
        return self._convert_scalar_indexer(obj, axis)
    try:
        self._validate_key(obj, axis)
        return obj
    except ValueError:
        raise ValueError('Can only index by location with a [{types}]'.
            format(types=self._valid_types))