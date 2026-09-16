def filter_genes_dispersion(data, flavor='seurat', min_disp=None, max_disp=
    None, min_mean=None, max_mean=None, n_bins=20, n_top_genes=None, log=
    True, copy=False):
    adata = data.copy() if copy else data
    set_initial_size(adata)
    if n_top_genes is not None and adata.n_vars < n_top_genes:
        logg.info(
            'Skip filtering by dispersion since number of variables are less than `n_top_genes`'
            )
    elif flavor is 'svr':
        mu = adata.X.mean(0).A1 if issparse(adata.X) else adata.X.mean(0)
        sigma = np.sqrt(adata.X.multiply(adata.X).mean(0).A1 - mu ** 2
            ) if issparse(adata.X) else adata.X.std(0)
        log_mu = np.log2(mu)
        log_cv = np.log2(sigma / mu)
        from sklearn.svm import SVR
        clf = SVR(gamma=150.0 / len(mu))
        clf.fit(log_mu[:, (None)], log_cv)
        score = log_cv - clf.predict(log_mu[:, (None)])
        nth_score = np.sort(score)[::-1][n_top_genes]
        adata._inplace_subset_var(score >= nth_score)
    else:
        from scanpy.api.pp import filter_genes_dispersion
        filter_genes_dispersion(adata, flavor=flavor, min_disp=min_disp,
            max_disp=max_disp, min_mean=min_mean, max_mean=max_mean, n_bins
            =n_bins, n_top_genes=n_top_genes, log=log)
    return adata if copy else None