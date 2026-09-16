def draw(self, layout, coord):
    params = copy(self.geom.params)
    params.update(self.stat.params)
    params['zorder'] = self.zorder
    self.data = self.geom.handle_na(self.data)
    self.geom.draw_layer(self.data, layout, coord, **params)