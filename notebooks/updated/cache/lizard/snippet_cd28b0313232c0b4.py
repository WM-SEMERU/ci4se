def unary_from_labels(labels, n_labels, gt_prob, zero_unsure=True):
    assert 0 < gt_prob < 1, '`gt_prob must be in (0,1).'
    labels = labels.flatten()
    n_energy = -np.log((1.0 - gt_prob) / (n_labels - 1))
    p_energy = -np.log(gt_prob)
    U = np.full((n_labels, len(labels)), n_energy, dtype='float32')
    U[labels - 1 if zero_unsure else labels, np.arange(U.shape[1])] = p_energy
    if zero_unsure:
        U[:, (labels == 0)] = -np.log(1.0 / n_labels)
    return U