def pysal_Geary(self, **kwargs):
    if self.weights is None:
        self.raster_weights(**kwargs)
    rasterf = self.raster.flatten()
    rasterf = rasterf[rasterf.mask == False]
    self.Geary = pysal.Geary(rasterf, self.weights, **kwargs)