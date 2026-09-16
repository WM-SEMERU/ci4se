def _index_param_value(num_samples, v, indices):
    if not _is_arraylike(v) or _num_samples(v) != num_samples:
        return v
    if sp.issparse(v):
        v = v.tocsr()
    return safe_indexing(v, indices)