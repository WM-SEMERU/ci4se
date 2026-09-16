def mask_negative(self):
    self.mask = np.logical_and(self.mask, ~(self.intensity < 0))