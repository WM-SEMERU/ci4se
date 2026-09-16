def heatmapf(func, scale=10, boundary=True, cmap=None, ax=None, scientific=
    False, style='triangular', colorbar=True, permutation=None, vmin=None,
    vmax=None, cbarlabel=None, cb_kwargs=None):
    data = dict()
    for i, j, k in simplex_iterator(scale=scale, boundary=boundary):
        data[i, j] = func(normalize([i, j, k]))
    ax = heatmap(data, scale, cmap=cmap, ax=ax, style=style, scientific=
        scientific, colorbar=colorbar, permutation=permutation, vmin=vmin,
        vmax=vmax, cbarlabel=cbarlabel, cb_kwargs=cb_kwargs)
    return ax