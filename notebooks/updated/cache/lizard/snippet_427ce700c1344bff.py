def add_chan(self, chan, color=None, values=None, limits_c=None, colormap=
    CHAN_COLORMAP, alpha=None, colorbar=False):
    if limits_c is None and self._chan_limits is not None:
        limits_c = self._chan_limits
    chan_colors, limits = _prepare_colors(color=color, values=values,
        limits_c=limits_c, colormap=colormap, alpha=alpha, chan=chan)
    self._chan_limits = limits
    xyz = chan.return_xyz()
    marker = Markers()
    marker.set_data(pos=xyz, size=CHAN_SIZE, face_color=chan_colors)
    self._add_mesh(marker)
    if colorbar:
        self._view.add(_colorbar_for_surf(colormap, limits))