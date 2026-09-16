def plot_lattice_vectors(lattice, ax=None, **kwargs):
    ax, fig, plt = get_ax3d_fig_plt(ax)
    if 'color' not in kwargs:
        kwargs['color'] = 'g'
    if 'linewidth' not in kwargs:
        kwargs['linewidth'] = 3
    vertex1 = lattice.get_cartesian_coords([0.0, 0.0, 0.0])
    vertex2 = lattice.get_cartesian_coords([1.0, 0.0, 0.0])
    ax.plot(*zip(vertex1, vertex2), **kwargs)
    vertex2 = lattice.get_cartesian_coords([0.0, 1.0, 0.0])
    ax.plot(*zip(vertex1, vertex2), **kwargs)
    vertex2 = lattice.get_cartesian_coords([0.0, 0.0, 1.0])
    ax.plot(*zip(vertex1, vertex2), **kwargs)
    return fig, ax