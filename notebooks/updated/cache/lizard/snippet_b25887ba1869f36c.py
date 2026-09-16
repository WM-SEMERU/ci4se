def convert_like(item, like):
    if isinstance(like, np.ndarray):
        return np.asanyarray(item, dtype=like.dtype)
    if isinstance(item, like.__class__) or is_none(like):
        return item
    if is_sequence(item) and len(item) == 1 and isinstance(item[0], like.
        __class__):
        return item[0]
    item = like.__class__(item)
    return item