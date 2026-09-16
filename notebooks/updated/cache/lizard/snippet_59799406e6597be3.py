def prepend_zeros(self, num):
    self.resize(len(self) + num)
    self.roll(num)
    self._epoch = self._epoch - num * self._delta_t