def _merge(self, key, value):
    method = self._merge_method(key)
    if method is not None:
        if method == 'update' and is_str(value):
            value = [value]
        if method == 'append' and isinstance(self[key], list) and isinstance(
            value, list):
            method = 'extend'
        getattr(self[key], method)(value)
    else:
        super(MergingDict, self).__setitem__(key, value)