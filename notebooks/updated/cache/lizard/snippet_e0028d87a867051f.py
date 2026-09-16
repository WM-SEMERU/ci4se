def add_size_scaled_points(self, longitude, latitude, data, shape='o',
    logplot=False, alpha=1.0, colour='b', smin=2.0, sscale=2.0, overlay=False):
    if logplot:
        data = np.log10(data.copy())
    x, y = self.m(longitude, latitude)
    self.m.scatter(x, y, marker=shape, s=smin + data ** sscale, c=colour,
        alpha=alpha, zorder=2)
    if not overlay:
        plt.show()