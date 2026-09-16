def join(self, other, on=None, how='left', lsuffix=None, rsuffix=None,
    algorithm='merge', is_on_sorted=True, is_on_unique=True):
    check_type(lsuffix, str)
    check_type(rsuffix, str)
    self_names = self._gather_column_names()
    other_names = other._gather_column_names()
    common_names = set(self_names).intersection(set(other_names))
    if len(common_names) > 0 and lsuffix is None and rsuffix is None:
        raise ValueError('Columns overlap but no suffixes supplied')
    lsuffix = '' if lsuffix is None else lsuffix
    rsuffix = '' if rsuffix is None else rsuffix
    return self.merge(other, how, on, (lsuffix, rsuffix), algorithm,
        is_on_sorted, is_on_unique)