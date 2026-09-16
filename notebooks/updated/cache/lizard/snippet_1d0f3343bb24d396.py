def recipe_seurat(adata, log=True, plot=False, copy=False):
    if copy:
        adata = adata.copy()
    pp.filter_cells(adata, min_genes=200)
    pp.filter_genes(adata, min_cells=3)
    pp.normalize_per_cell(adata, counts_per_cell_after=10000.0)
    filter_result = filter_genes_dispersion(adata.X, min_mean=0.0125,
        max_mean=3, min_disp=0.5, log=not log)
    if plot:
        from ..plotting import _preprocessing as ppp
        ppp.filter_genes_dispersion(filter_result, log=not log)
    adata._inplace_subset_var(filter_result.gene_subset)
    if log:
        pp.log1p(adata)
    pp.scale(adata, max_value=10)
    return adata if copy else None