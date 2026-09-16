def matrix_to_pair_dictionary(X, row_keys=None, column_keys=None, filter_fn
    =None):
    n_rows, n_cols = X.shape
    if row_keys is None:
        row_keys = {i: i for i in range(n_rows)}
    if column_keys is None:
        if n_rows == n_cols:
            column_keys = row_keys
        else:
            column_keys = {j: j for j in range(n_cols)}
    if len(row_keys) != n_rows:
        raise ValueError('Need %d row keys but got list of length %d' % (
            n_rows, len(row_keys)))
    if len(column_keys) != n_cols:
        raise ValueError('Need %d column keys but got list of length %d' %
            (n_cols, len(column_keys)))
    result_dict = {}
    for i, X_i in enumerate(X):
        row_key = row_keys[i]
        for j, X_ij in enumerate(X_i):
            if filter_fn and not filter_fn(X_ij):
                continue
            column_key = column_keys[j]
            key_pair = row_key, column_key
            result_dict[key_pair] = X_ij
    return result_dict