def set_block(arr, arr_block):
    nr_col = arr.shape[1]
    nr_row = arr.shape[0]
    nr_col_block = arr_block.shape[1]
    nr_row_block = arr_block.shape[0]
    if np.mod(nr_row, nr_row_block) or np.mod(nr_col, nr_col_block):
        raise ValueError(
            'Number of rows/columns of the input array must be a multiple of block shape'
            )
    if nr_row / nr_row_block != nr_col / nr_col_block:
        raise ValueError(
            'Block array can not be filled as diagonal blocks in the given array'
            )
    arr_out = arr.copy()
    for row_ind in range(int(nr_row / nr_row_block)):
        row_start = row_ind * nr_row_block
        row_end = nr_row_block + nr_row_block * row_ind
        col_start = row_ind * nr_col_block
        col_end = nr_col_block + nr_col_block * row_ind
        arr_out[row_start:row_end, col_start:col_end] = arr_block
    return arr_out