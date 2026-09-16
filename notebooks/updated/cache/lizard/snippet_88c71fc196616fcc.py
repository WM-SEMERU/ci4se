def truncate(self, before=None, after=None, axis=None, copy=True):
    if axis is None:
        axis = self._stat_axis_number
    axis = self._get_axis_number(axis)
    ax = self._get_axis(axis)
    if not ax.is_monotonic_increasing and not ax.is_monotonic_decreasing:
        raise ValueError('truncate requires a sorted index')
    if ax.is_all_dates:
        from pandas.core.tools.datetimes import to_datetime
        before = to_datetime(before)
        after = to_datetime(after)
    if before is not None and after is not None:
        if before > after:
            raise ValueError('Truncate: %s must be after %s' % (after, before))
    slicer = [slice(None, None)] * self._AXIS_LEN
    slicer[axis] = slice(before, after)
    result = self.loc[tuple(slicer)]
    if isinstance(ax, MultiIndex):
        setattr(result, self._get_axis_name(axis), ax.truncate(before, after))
    if copy:
        result = result.copy()
    return result