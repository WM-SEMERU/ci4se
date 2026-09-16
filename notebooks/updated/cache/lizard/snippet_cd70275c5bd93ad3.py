def _add_sphere(ax):
    u, v = np.mgrid[0:2 * np.pi:20.0j, 0:np.pi:10.0j]
    x = np.cos(u) * np.sin(v)
    y = np.sin(u) * np.sin(v)
    z = np.cos(v)
    ax.plot_wireframe(x, y, z, color='grey', linewidth=0.2)
    return ax