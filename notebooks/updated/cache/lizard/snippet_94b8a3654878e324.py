def compute_spectrogram(G, atom=None, M=100, **kwargs):
    r
    if not atom:

        def atom(x):
            return np.exp(-M * (x / G.lmax) ** 2)
    scale = np.linspace(0, G.lmax, M)
    spectr = np.empty((G.N, M))
    for shift_idx in range(M):
        shift_filter = filters.Filter(G, lambda x: atom(x - scale[shift_idx]))
        tig = compute_norm_tig(shift_filter, **kwargs).squeeze() ** 2
        spectr[:, (shift_idx)] = tig
    G.spectr = spectr
    return spectr