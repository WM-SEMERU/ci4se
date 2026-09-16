def _hash_data(hasher, data):
    _hasher = hasher.copy()
    _hasher.update(data)
    return _hasher.finalize()