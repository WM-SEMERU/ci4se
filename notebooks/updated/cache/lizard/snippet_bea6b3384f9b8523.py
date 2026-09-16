def _get_nan_block_id(partition_class, n_row=1, n_col=1, transpose=False):
    global _NAN_BLOCKS
    if transpose:
        n_row, n_col = n_col, n_row
    shape = n_row, n_col
    if shape not in _NAN_BLOCKS:
        arr = np.tile(np.array(np.NaN), shape)
        _NAN_BLOCKS[shape] = partition_class.put(pandas.DataFrame(data=arr))
    return _NAN_BLOCKS[shape]