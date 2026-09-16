def _advanced_indexer_subspaces(key):
    if not isinstance(key, tuple):
        key = key,
    advanced_index_positions = [i for i, k in enumerate(key) if not
        isinstance(k, slice)]
    if not advanced_index_positions or not _is_contiguous(
        advanced_index_positions):
        return (), ()
    non_slices = [k for k in key if not isinstance(k, slice)]
    ndim = len(np.broadcast(*non_slices).shape)
    mixed_positions = advanced_index_positions[0] + np.arange(ndim)
    vindex_positions = np.arange(ndim)
    return mixed_positions, vindex_positions