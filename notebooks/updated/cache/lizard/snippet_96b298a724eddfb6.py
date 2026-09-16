def plot_points(points, lattice=None, coords_are_cartesian=False, fold=
    False, ax=None, **kwargs):
    ax, fig, plt = get_ax3d_fig_plt(ax)
    if 'color' not in kwargs:
        kwargs['color'] = 'b'
    if (not coords_are_cartesian or fold) and lattice is None:
        raise ValueError(
            'coords_are_cartesian False or fold True require the lattice')
    for p in points:
        if fold:
            p = fold_point(p, lattice, coords_are_cartesian=
                coords_are_cartesian)
        elif not coords_are_cartesian:
            p = lattice.get_cartesian_coords(p)
        ax.scatter(*p, **kwargs)
    return fig, ax