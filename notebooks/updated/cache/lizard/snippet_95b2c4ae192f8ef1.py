def dpt_timeseries(adata, color_map=None, show=None, save=None, as_heatmap=True
    ):
    if adata.n_vars > 100:
        logg.warn(
            'Plotting more than 100 genes might take some while,consider selecting only highly variable genes, for example.'
            )
    if as_heatmap:
        timeseries_as_heatmap(adata.X[adata.obs['dpt_order_indices'].values
            ], var_names=adata.var_names, highlightsX=adata.uns[
            'dpt_changepoints'], color_map=color_map)
    else:
        timeseries(adata.X[adata.obs['dpt_order_indices'].values],
            var_names=adata.var_names, highlightsX=adata.uns[
            'dpt_changepoints'], xlim=[0, 1.3 * adata.X.shape[0]])
    pl.xlabel('dpt order')
    utils.savefig_or_show('dpt_timeseries', save=save, show=show)