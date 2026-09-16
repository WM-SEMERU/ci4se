def scatter_group(ax, key, imask, adata, Y, projection='2d', size=3, alpha=None
    ):
    mask = adata.obs[key].cat.categories[imask] == adata.obs[key].values
    color = adata.uns[key + '_colors'][imask]
    if not isinstance(color[0], str):
        from matplotlib.colors import rgb2hex
        color = rgb2hex(adata.uns[key + '_colors'][imask])
    if not is_color_like(color):
        raise ValueError('"{}" is not a valid matplotlib color.'.format(color))
    data = [Y[mask, 0], Y[mask, 1]]
    if projection == '3d':
        data.append(Y[mask, 2])
    ax.scatter(*data, marker='.', alpha=alpha, c=color, edgecolors='none',
        s=size, label=adata.obs[key].cat.categories[imask], rasterized=
        settings._vector_friendly)
    return mask