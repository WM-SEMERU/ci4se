def pca_loadings(adata, components=None, show=None, save=None):
    if components is None:
        components = [1, 2, 3]
    elif isinstance(components, str):
        components = components.split(',')
    components = np.array(components) - 1
    ranking(adata, 'varm', 'PCs', indices=components)
    utils.savefig_or_show('pca_loadings', show=show, save=save)