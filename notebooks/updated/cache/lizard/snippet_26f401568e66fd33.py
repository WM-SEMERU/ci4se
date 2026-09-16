def velocity_confidence_transition(data, vkey='velocity', scale=10, copy=False
    ):
    adata = data.copy() if copy else data
    if vkey not in adata.layers.keys():
        raise ValueError('You need to run `tl.velocity` first.')
    idx = np.array(adata.var[vkey + '_genes'].values, dtype=bool)
    T = transition_matrix(adata, vkey=vkey, scale=scale)
    dX = T.dot(adata.layers['Ms'][:, (idx)]) - adata.layers['Ms'][:, (idx)]
    dX -= dX.mean(1)[:, (None)]
    V = adata.layers[vkey][:, (idx)].copy()
    V -= V.mean(1)[:, (None)]
    adata.obs[vkey + '_confidence_transition'] = prod_sum_var(dX, V) / (norm
        (dX) * norm(V))
    logg.hint("added '" + vkey + "_confidence_transition' (adata.obs)")
    return adata if copy else None