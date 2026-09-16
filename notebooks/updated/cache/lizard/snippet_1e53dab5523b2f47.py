def locate_fixed_differences(ac1, ac2):
    ac1 = asarray_ndim(ac1, 2)
    ac2 = asarray_ndim(ac2, 2)
    check_dim0_aligned(ac1, ac2)
    ac1, ac2 = ensure_dim1_aligned(ac1, ac2)
    pac = np.dstack([ac1, ac2])
    pan = np.sum(pac, axis=1)
    npa = np.sum(pac > 0, axis=2)
    non_missing = np.all(pan > 0, axis=1)
    no_shared_alleles = np.all(npa <= 1, axis=1)
    return non_missing & no_shared_alleles