def ShowErrorBarCaps(ax):
    for ch in ax.get_children():
        if str(ch).startswith('Line2D'):
            ch.set_markeredgewidth(1)
            ch.set_markersize(8)