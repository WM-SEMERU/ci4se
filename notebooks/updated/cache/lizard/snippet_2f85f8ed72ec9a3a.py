def zoom_to(self, zoomlevel, no_reset=False):
    scale_x, scale_y = self.zoom.calc_scale(zoomlevel)
    self._scale_to(scale_x, scale_y, no_reset=no_reset)