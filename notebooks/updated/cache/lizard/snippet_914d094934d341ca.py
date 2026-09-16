def tz_localize(self, tz, axis=0, level=None, copy=True, ambiguous='raise',
    nonexistent='raise'):
    nonexistent_options = 'raise', 'NaT', 'shift_forward', 'shift_backward'
    if nonexistent not in nonexistent_options and not isinstance(nonexistent,
        timedelta):
        raise ValueError(
            "The nonexistent argument must be one of 'raise', 'NaT', 'shift_forward', 'shift_backward' or a timedelta object"
            )
    axis = self._get_axis_number(axis)
    ax = self._get_axis(axis)

    def _tz_localize(ax, tz, ambiguous, nonexistent):
        if not hasattr(ax, 'tz_localize'):
            if len(ax) > 0:
                ax_name = self._get_axis_name(axis)
                raise TypeError(
                    '%s is not a valid DatetimeIndex or PeriodIndex' % ax_name)
            else:
                ax = DatetimeIndex([], tz=tz)
        else:
            ax = ax.tz_localize(tz, ambiguous=ambiguous, nonexistent=
                nonexistent)
        return ax
    if isinstance(ax, MultiIndex):
        level = ax._get_level_number(level)
        new_level = _tz_localize(ax.levels[level], tz, ambiguous, nonexistent)
        ax = ax.set_levels(new_level, level=level)
    else:
        if level not in (None, 0, ax.name):
            raise ValueError('The level {0} is not valid'.format(level))
        ax = _tz_localize(ax, tz, ambiguous, nonexistent)
    result = self._constructor(self._data, copy=copy)
    result = result.set_axis(ax, axis=axis, inplace=False)
    return result.__finalize__(self)