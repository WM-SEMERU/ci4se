def shift_to_origin(self, **kwargs):
    self.coordinates = shift_com(self.elements, self.coordinates, **kwargs)
    self._update()