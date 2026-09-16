def validate_min_itemsize(self, min_itemsize):
    if min_itemsize is None:
        return
    if not isinstance(min_itemsize, dict):
        return
    q = self.queryables()
    for k, v in min_itemsize.items():
        if k == 'values':
            continue
        if k not in q:
            raise ValueError(
                'min_itemsize has the key [{key}] which is not an axis or data_column'
                .format(key=k))