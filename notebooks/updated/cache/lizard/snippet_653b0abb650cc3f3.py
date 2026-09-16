def check_precomputed_distance_matrix(X):
    tmp = X.copy()
    tmp[np.isinf(tmp)] = 1
    check_array(tmp)