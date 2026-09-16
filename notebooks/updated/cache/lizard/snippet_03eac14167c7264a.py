def run_diff_umap(self, use_rep='X_pca', metric='euclidean', n_comps=15,
    method='gauss', **kwargs):
    import scanpy.api as sc
    sc.pp.neighbors(self.adata, use_rep=use_rep, n_neighbors=self.k, metric
        =self.distance, method=method)
    sc.tl.diffmap(self.adata, n_comps=n_comps)
    sc.pp.neighbors(self.adata, use_rep='X_diffmap', n_neighbors=self.k,
        metric='euclidean', method=method)
    if 'X_umap' in self.adata.obsm.keys():
        self.adata.obsm['X_umap_sam'] = self.adata.obsm['X_umap']
    sc.tl.umap(self.adata, min_dist=0.1, copy=False)