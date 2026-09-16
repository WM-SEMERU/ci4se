def _plot_filter(filters, n, eigenvalues, sum, title, ax, **kwargs):
    r
    if eigenvalues is None:
        eigenvalues = filters.G._e is not None
    if sum is None:
        sum = filters.n_filters > 1
    if title is None:
        title = repr(filters)
    return _plt_plot_filter(filters, n=n, eigenvalues=eigenvalues, sum=sum,
        title=title, ax=ax, **kwargs)