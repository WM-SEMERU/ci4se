def plot_shade_mask(ax, ind, mask, facecolor='gray', alpha=0.5):
    ymin, ymax = ax.get_ylim()
    ax.fill_between(ind, ymin, ymax, where=mask, facecolor=facecolor, alpha
        =alpha)
    return ax