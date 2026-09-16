def _fill_untouched(idx, ret, fill_value):
    untouched = np.ones_like(ret, dtype=bool)
    untouched[idx] = False
    ret[untouched] = fill_value