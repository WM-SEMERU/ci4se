def draw_identity_line(ax=None, dynamic=True, **kwargs):
    ax = ax or plt.gca()
    if 'c' not in kwargs and 'color' not in kwargs:
        kwargs['color'] = LINE_COLOR
    if 'alpha' not in kwargs:
        kwargs['alpha'] = 0.5
    identity, = ax.plot([], [], **kwargs)

    def callback(ax):
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()
        data = max(xlim[0], ylim[0]), min(xlim[1], ylim[1])
        identity.set_data(data, data)
    callback(ax)
    if dynamic:
        ax.callbacks.connect('xlim_changed', callback)
        ax.callbacks.connect('ylim_changed', callback)
    return ax