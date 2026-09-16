def _collapse_to_cwl_record_single(data, want_attrs, input_files):
    out = {}
    for key in want_attrs:
        key_parts = key.split('__')
        out[key] = _to_cwl(tz.get_in(key_parts, data), input_files)
    return out