def filter_genes_cv_deprecated(X, Ecutoff, cvFilter):
    if issparse(X):
        raise ValueError(
            'Not defined for sparse input. See `filter_genes_dispersion`.')
    mean_filter = np.mean(X, axis=0) > Ecutoff
    var_filter = np.std(X, axis=0) / (np.mean(X, axis=0) + 0.0001) > cvFilter
    gene_subset = np.nonzero(np.all([mean_filter, var_filter], axis=0))[0]
    return gene_subset