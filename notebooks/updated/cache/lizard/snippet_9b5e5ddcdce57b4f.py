def get_split_adjusted_asof_idx(self, dates):
    split_adjusted_asof_idx = dates.searchsorted(self._split_adjusted_asof)
    if split_adjusted_asof_idx == len(dates):
        split_adjusted_asof_idx = len(dates) - 1
    elif self._split_adjusted_asof < dates[0].tz_localize(None):
        split_adjusted_asof_idx = -1
    return split_adjusted_asof_idx