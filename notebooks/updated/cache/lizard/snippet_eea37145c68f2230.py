def _contingency_matrix(reference_indices, estimated_indices):
    ref_classes, ref_class_idx = np.unique(reference_indices,
        return_inverse=True)
    est_classes, est_class_idx = np.unique(estimated_indices,
        return_inverse=True)
    n_ref_classes = ref_classes.shape[0]
    n_est_classes = est_classes.shape[0]
    return scipy.sparse.coo_matrix((np.ones(ref_class_idx.shape[0]), (
        ref_class_idx, est_class_idx)), shape=(n_ref_classes, n_est_classes
        ), dtype=np.int).toarray()