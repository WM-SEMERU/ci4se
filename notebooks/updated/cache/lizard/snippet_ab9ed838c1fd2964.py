def _plot_area_source(self, source, border='k-', border_width=1.0):
    lons = np.hstack([source.geometry.lons, source.geometry.lons[0]])
    lats = np.hstack([source.geometry.lats, source.geometry.lats[0]])
    x, y = self.m(lons, lats)
    self.m.plot(x, y, border, linewidth=border_width)