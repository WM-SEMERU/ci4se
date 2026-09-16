def plot_legend(ax, no_legend=True, legend_arg=None):
    legend_arg = dict_if_none(legend_arg)
    if not no_legend:
        ax.legend(**legend_arg)