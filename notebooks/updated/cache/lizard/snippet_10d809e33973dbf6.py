def label_subplot(ax=None, x=0.5, y=-0.25, text='(a)', **kwargs):
    if ax is None:
        ax = plt.gca()
    ax.text(x=x, y=y, s=text, transform=ax.transAxes, horizontalalignment=
        'center', verticalalignment='top', **kwargs)