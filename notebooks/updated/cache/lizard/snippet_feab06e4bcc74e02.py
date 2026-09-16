def knn_impute_with_argpartition(X, missing_mask, k, verbose=False,
    print_interval=100):
    start_t = time.time()
    n_rows, n_cols = X.shape
    missing_mask_column_major = np.asarray(missing_mask, order='F')
    X_row_major, D, effective_infinity = knn_initialize(X, missing_mask,
        verbose=verbose)
    D_reciprocal = 1.0 / D
    dot = np.dot
    array = np.array
    argpartition = np.argpartition
    for i in range(n_rows):
        missing_indices = np.where(missing_mask[i])[0]
        if verbose and i % print_interval == 0:
            print('Imputing row %d/%d with %d missing, elapsed time: %0.3f' %
                (i + 1, n_rows, len(missing_indices), time.time() - start_t))
        d = D[(i), :]
        inv_d = D_reciprocal[(i), :]
        for j in missing_indices:
            d_copy = d.copy()
            d_copy[missing_mask_column_major[:, (j)]] = effective_infinity
            neighbor_indices = argpartition(d_copy, k)[:k]
            if d_copy[neighbor_indices].max() >= effective_infinity:
                neighbor_indices = array([neighbor_index for neighbor_index in
                    neighbor_indices if d_copy[neighbor_index] <
                    effective_infinity])
            n_current_neighbors = len(neighbor_indices)
            if n_current_neighbors > 0:
                neighbor_weights = inv_d[neighbor_indices]
                X_row_major[i, j] = dot(X[:, (j)][neighbor_indices],
                    neighbor_weights) / neighbor_weights.sum()
    return X_row_major