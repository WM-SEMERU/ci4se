def merge_limits(axes, xlim=True, ylim=True):
    xlims = list()
    ylims = list()
    for ax in axes:
        [xlims.append(lim) for lim in ax.get_xlim()]
        [ylims.append(lim) for lim in ax.get_ylim()]
    for ax in axes:
        if xlim:
            ax.set_xlim(min(xlims), max(xlims))
        if ylim:
            ax.set_ylim(min(ylims), max(ylims))
    return None