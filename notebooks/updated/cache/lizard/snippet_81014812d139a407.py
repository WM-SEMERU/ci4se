def cds_column_replace(source, data):
    current_length = [len(v) for v in source.data.values() if isinstance(v,
        (list, np.ndarray))]
    new_length = [len(v) for v in data.values() if isinstance(v, (list, np.
        ndarray))]
    untouched = [k for k in source.data if k not in data]
    return bool(untouched and current_length and new_length and 
        current_length[0] != new_length[0])