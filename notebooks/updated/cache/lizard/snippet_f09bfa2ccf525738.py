def _get_na_values(col, na_values, na_fvalues, keep_default_na):
    if isinstance(na_values, dict):
        if col in na_values:
            return na_values[col], na_fvalues[col]
        else:
            if keep_default_na:
                return _NA_VALUES, set()
            return set(), set()
    else:
        return na_values, na_fvalues