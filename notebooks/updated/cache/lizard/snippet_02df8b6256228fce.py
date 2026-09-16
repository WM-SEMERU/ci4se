def colorbar_hack(ax, vmin, vmax, cmap, scientific=False, cbarlabel=None,
    **kwargs):
    norm = plt.Normalize(vmin=vmin, vmax=vmax)
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm._A = []
    cb = plt.colorbar(sm, ax=ax, **kwargs)
    if cbarlabel is not None:
        cb.set_label(cbarlabel)
    if scientific:
        cb.locator = matplotlib.ticker.LinearLocator(numticks=7)
        cb.formatter = matplotlib.ticker.ScalarFormatter()
        cb.formatter.set_powerlimits((0, 0))
        cb.update_ticks()