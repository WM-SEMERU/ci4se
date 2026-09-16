def _scale_mesh(self, scale):
    pos_ks = ['vertices', 'centers']
    self.update_columns_dict({k: (self[k] * scale) for k in pos_ks})
    self.update_columns(areas=self.areas * scale ** 2)
    self._volume *= scale ** 3
    if self._area is not None:
        self._area += scale ** 2