def _ycbcr2rgb(self, mode):
    self._check_modes(('YCbCr', 'YCbCrA'))
    self.channels[0], self.channels[1], self.channels[2] = ycbcr2rgb(self.
        channels[0], self.channels[1], self.channels[2])
    if self.fill_value is not None:
        self.fill_value[0:3] = ycbcr2rgb(self.fill_value[0], self.
            fill_value[1], self.fill_value[2])
    self.mode = mode