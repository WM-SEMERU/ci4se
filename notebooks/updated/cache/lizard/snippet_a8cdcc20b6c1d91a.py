def add_mpl_colorscale(fig, heatmap_gs, ax_map, params, title=None):
    cbticks = [(params.vmin + e * params.vdiff) for e in (0, 0.25, 0.5, 
        0.75, 1)]
    if params.vmax > 10:
        exponent = int(floor(log10(params.vmax))) - 1
        cbticks = [int(round(e, -exponent)) for e in cbticks]
    scale_subplot = gridspec.GridSpecFromSubplotSpec(1, 3, subplot_spec=
        heatmap_gs[0, 0], wspace=0.0, hspace=0.0)
    scale_ax = fig.add_subplot(scale_subplot[0, 1])
    cbar = fig.colorbar(ax_map, scale_ax, ticks=cbticks)
    if title:
        cbar.set_label(title, fontsize=6)
    cbar.ax.yaxis.set_ticks_position('left')
    cbar.ax.yaxis.set_label_position('left')
    cbar.ax.tick_params(labelsize=6)
    cbar.outline.set_linewidth(0)
    return cbar