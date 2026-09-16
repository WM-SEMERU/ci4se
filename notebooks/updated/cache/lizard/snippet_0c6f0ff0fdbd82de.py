def plot_heatmap(data, title='Heatmap', show_legend=True, show_labels=True,
    label_fmt='.2f', vmin=None, vmax=None, figsize=None, label_color='w',
    cmap='RdBu', **kwargs):
    fig, ax = plt.subplots(figsize=figsize)
    heatmap = ax.pcolor(data, vmin=vmin, vmax=vmax, cmap=cmap)
    ax.invert_yaxis()
    if title is not None:
        plt.title(title)
    if show_legend:
        fig.colorbar(heatmap)
    if show_labels:
        vals = data.values
        for x in range(data.shape[0]):
            for y in range(data.shape[1]):
                plt.text(x + 0.5, y + 0.5, format(vals[y, x], label_fmt),
                    horizontalalignment='center', verticalalignment=
                    'center', color=label_color)
    plt.yticks(np.arange(0.5, len(data.index), 1), data.index)
    plt.xticks(np.arange(0.5, len(data.columns), 1), data.columns)
    return plt