def imagesc(data, title=None, fig='current', ax=None):
    ax = _get_axis(fig, ax, False)
    ax.imshow(data, interpolation='nearest', aspect='auto')
    if title:
        ax.set_title(title)
    return plt.show