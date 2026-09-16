def record_diff(old, new):
    old, new = _norm_json_params(old, new)
    return json_delta.diff(new, old, verbose=False)