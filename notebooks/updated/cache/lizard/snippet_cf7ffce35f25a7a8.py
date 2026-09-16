def plot_pole(map_axis, plon, plat, A95, label='', color='k', edgecolor='k',
    marker='o', markersize=20, legend='no'):
    if not has_cartopy:
        print('-W- cartopy must be installed to run ipmag.plot_pole')
        return
    A95_km = A95 * 111.32
    map_axis.scatter(plon, plat, marker=marker, color=color, edgecolors=
        edgecolor, s=markersize, label=label, zorder=101, transform=ccrs.
        Geodetic())
    equi(map_axis, plon, plat, A95_km, color)
    if legend == 'yes':
        plt.legend(loc=2)