def _embedding_tsne(matrix, dimensions=3, early_exaggeration=12.0, method=
    'barnes_hut', perplexity=30, learning_rate=200, n_iter=1000):
    tsne = sklearn.manifold.TSNE(n_components=dimensions, metric=
        'precomputed', early_exaggeration=early_exaggeration, method=method,
        perplexity=perplexity, learning_rate=learning_rate, n_iter=1000)
    return tsne.fit_transform(matrix)