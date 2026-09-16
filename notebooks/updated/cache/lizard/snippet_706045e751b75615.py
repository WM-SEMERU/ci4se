def annotate_subplot(ax, ncols=1, nrows=1, letter='a', linear_offset=0.075,
    fontsize=8):
    ax.text(-ncols * linear_offset, 1 + nrows * linear_offset, letter,
        horizontalalignment='center', verticalalignment='center', fontsize=
        fontsize, fontweight='demibold', transform=ax.transAxes)