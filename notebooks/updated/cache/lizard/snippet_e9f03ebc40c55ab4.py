def sort_index(self, axis=0, level=None, ascending=True, inplace=False,
    kind='quicksort', na_position='last', sort_remaining=True):
    inplace = validate_bool_kwarg(inplace, 'inplace')
    axis = self._get_axis_number(axis)
    axis_name = self._get_axis_name(axis)
    labels = self._get_axis(axis)
    if level is not None:
        raise NotImplementedError('level is not implemented')
    if inplace:
        raise NotImplementedError('inplace is not implemented')
    sort_index = labels.argsort()
    if not ascending:
        sort_index = sort_index[::-1]
    new_axis = labels.take(sort_index)
    return self.reindex(**{axis_name: new_axis})