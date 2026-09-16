def embedding(self, dimensions, method, **kwargs):
    errors.optioncheck(method, ['cmds', 'kpca', 'mmds', 'nmmds', 'spectral',
        'tsne'])
    if method == 'cmds':
        array = _embedding_classical_mds(self.to_array(), dimensions, **kwargs)
    elif method == 'kpca':
        array = _embedding_kernel_pca(self.to_array(), dimensions, **kwargs)
    elif method == 'mmds':
        array = _embedding_metric_mds(self.to_array(), dimensions)
    elif method == 'nmmds':
        array = _embedding_nonmetric_mds(self.to_array(), dimensions, **kwargs)
    elif method == 'spectral':
        array = _embedding_spectral(self.to_array(), dimensions, **kwargs)
    elif method == 'tsne':
        array = _embedding_tsne(self.to_array(), dimensions, **kwargs)
    return CoordinateMatrix(array, names=self.df.index)