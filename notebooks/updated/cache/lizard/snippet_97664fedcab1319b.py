def zoom(ax, xy='x', factor=1):
    limits = ax.get_xlim() if xy == 'x' else ax.get_ylim()
    new_limits = 0.5 * (limits[0] + limits[1]) + 1.0 / factor * np.array((-
        0.5, 0.5)) * (limits[1] - limits[0])
    if xy == 'x':
        ax.set_xlim(new_limits)
    else:
        ax.set_ylim(new_limits)