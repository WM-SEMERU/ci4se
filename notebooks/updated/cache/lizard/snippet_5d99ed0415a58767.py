def mpl_outside_legend(ax, **kwargs):
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.75, box.height])
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1), **kwargs)