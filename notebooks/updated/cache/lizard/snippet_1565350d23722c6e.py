def log1p(data, copy=False):
    adata = data.copy() if copy else data
    X = (adata.X.data if issparse(adata.X) else adata.X) if isinstance(adata,
        AnnData) else adata
    np.log1p(X, out=X)
    return adata if copy else None