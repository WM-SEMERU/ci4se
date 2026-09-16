def stretch(self, scale_factor, callback=True):
    self.scale_pct *= scale_factor
    self.scale_and_shift(self.scale_pct, 0.0, callback=callback)