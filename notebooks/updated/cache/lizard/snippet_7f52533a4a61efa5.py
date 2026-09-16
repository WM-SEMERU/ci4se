def _paint_hue_legend(ax, categories, cmap, legend_labels, legend_kwargs,
    figure=False):
    patches = []
    for value, cat in enumerate(categories):
        patches.append(mpl.lines.Line2D([0], [0], linestyle='none', marker=
            'o', markersize=10, markerfacecolor=cmap.to_rgba(value)))
    if not legend_kwargs:
        legend_kwargs = dict()
    target = ax.figure if figure else ax
    if legend_labels:
        target.legend(patches, legend_labels, numpoints=1, fancybox=True,
            **legend_kwargs)
    else:
        target.legend(patches, categories, numpoints=1, fancybox=True, **
            legend_kwargs)