def _get_val(val, full=False):
    try:
        val = val.strip()
    except:
        pass
    logging.debug('%s, type=%s', val, type(val))
    if isinstance(val, float):
        return val
    if isinstance(val, int):
        return val
    if isinstance(val, np.ndarray):
        return list(val)
    try:
        val = float(val)
        return val
    except:
        pass
    try:
        val = int(val)
        return val
    except:
        pass
    if type(val) == pd.DataFrame:
        if full:
            return val
        newval = []
        values = val.values
        for v in values:
            newv = _get_val(v)
            if type(newv) == list:
                newval.extend(newv)
            else:
                newval.append(newv)
        val = newval
    elif type(val) == dict:
        if full:
            return val
        newval = []
        for v in val.values():
            newv = _get_val(v)
            if type(newv) == list:
                newval.extend(newv)
            else:
                newval.append(newv)
        val = newval
    elif type(val) == list or type(val) == np.ndarray:
        newval = []
        for arr_val in val:
            v = _get_val(arr_val)
            newval.append(v)
        val = newval
    return val