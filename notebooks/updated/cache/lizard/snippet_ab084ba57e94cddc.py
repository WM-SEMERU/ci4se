def setup(self, layers, plot):
    data = [l.data for l in layers]
    self.facet = plot.facet
    self.facet.setup_params(data)
    data = self.facet.setup_data(data)
    self.coord = plot.coordinates
    self.coord.setup_params(data)
    data = self.coord.setup_data(data)
    data = self.facet.setup_data(data)
    self.layout = self.facet.compute_layout(data)
    self.layout = self.coord.setup_layout(self.layout)
    self.check_layout()
    for layer, ldata in zip(layers, data):
        layer.data = self.facet.map(ldata, self.layout)