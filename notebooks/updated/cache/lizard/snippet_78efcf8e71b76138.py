def bss_eval_sources(reference_sources, estimated_sources,
    compute_permutation=True):
    sdr, isr, sir, sar, perm = bss_eval(reference_sources,
        estimated_sources, window=np.inf, hop=np.inf, compute_permutation=
        compute_permutation, filters_len=512, framewise_filters=True,
        bsseval_sources_version=True)
    return sdr, sir, sar, perm