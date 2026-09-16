def _adjusted_rand_index(reference_indices, estimated_indices):
    n_samples = len(reference_indices)
    ref_classes = np.unique(reference_indices)
    est_classes = np.unique(estimated_indices)
    if ref_classes.shape[0] == est_classes.shape[0] == 1 or ref_classes.shape[0
        ] == est_classes.shape[0] == 0 or ref_classes.shape[0
        ] == est_classes.shape[0] == len(reference_indices):
        return 1.0
    contingency = _contingency_matrix(reference_indices, estimated_indices)
    sum_comb_c = sum(scipy.special.comb(n_c, 2, exact=1) for n_c in
        contingency.sum(axis=1))
    sum_comb_k = sum(scipy.special.comb(n_k, 2, exact=1) for n_k in
        contingency.sum(axis=0))
    sum_comb = sum(scipy.special.comb(n_ij, 2, exact=1) for n_ij in
        contingency.flatten())
    prod_comb = sum_comb_c * sum_comb_k / float(scipy.special.comb(
        n_samples, 2))
    mean_comb = (sum_comb_k + sum_comb_c) / 2.0
    return (sum_comb - prod_comb) / (mean_comb - prod_comb)