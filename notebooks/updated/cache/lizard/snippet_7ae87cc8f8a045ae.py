def _symmetrize_correlograms(correlograms):
    n_clusters, _, n_bins = correlograms.shape
    assert n_clusters == _
    correlograms[..., 0] = np.maximum(correlograms[..., 0], correlograms[
        ..., 0].T)
    sym = correlograms[(...), 1:][(...), ::-1]
    sym = np.transpose(sym, (1, 0, 2))
    return np.dstack((sym, correlograms))