def _concat_same_dtype(self, to_concat, name):
    attribs = self._get_attributes_dict()
    attribs['name'] = name
    if len({str(x.dtype) for x in to_concat}) != 1:
        raise ValueError('to_concat must have the same tz')
    new_data = type(self._values)._concat_same_type(to_concat).asi8
    is_diff_evenly_spaced = len(unique_deltas(new_data)) == 1
    if not is_period_dtype(self) and not is_diff_evenly_spaced:
        attribs['freq'] = None
    return self._simple_new(new_data, **attribs)