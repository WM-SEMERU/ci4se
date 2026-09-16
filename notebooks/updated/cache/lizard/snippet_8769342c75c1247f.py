def _next_raw_dimension(self):
    dimension_dicts = self._dimension_dicts
    this_idx = dimension_dicts.index(self._dimension_dict)
    if this_idx > len(dimension_dicts) - 2:
        return None
    return _RawDimension(dimension_dicts[this_idx + 1], self._dimension_dicts)