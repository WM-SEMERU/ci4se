def matrix(matrix, xlabel=None, ylabel=None, xticks=None, yticks=None,
    title=None, colorbar_shrink=0.5, color_map=None, show=None, save=None,
    ax=None):
    if ax is None:
        ax = pl.gca()
    img = ax.imshow(matrix, cmap=color_map)
    if xlabel is not None:
        ax.set_xlabel(xlabel)
    if ylabel is not None:
        ax.set_ylabel(ylabel)
    if title is not None:
        ax.set_title(title)
    if xticks is not None:
        ax.set_xticks(range(len(xticks)), xticks, rotation='vertical')
    if yticks is not None:
        ax.set_yticks(range(len(yticks)), yticks)
    pl.colorbar(img, shrink=colorbar_shrink, ax=ax)
    savefig_or_show('matrix', show=show, save=save)