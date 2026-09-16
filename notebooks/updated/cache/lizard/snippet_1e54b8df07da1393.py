def plot_sphere(ax, center, radius, color='black', alpha=1.0,
    linspace_count=_LINSPACE_COUNT):
    u = np.linspace(0, 2 * np.pi, linspace_count)
    v = np.linspace(0, np.pi, linspace_count)
    sin_v = np.sin(v)
    x = center[0] + radius * np.outer(np.cos(u), sin_v)
    y = center[1] + radius * np.outer(np.sin(u), sin_v)
    z = center[2] + radius * np.outer(np.ones_like(u), np.cos(v))
    ax.plot_surface(x, y, z, linewidth=0.0, color=color, alpha=alpha)