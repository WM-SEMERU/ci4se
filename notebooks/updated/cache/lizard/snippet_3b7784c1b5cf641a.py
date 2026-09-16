def set_interrupt_limits(self, low, high):
    self._device.write8(4, low & 255)
    self._device.write8(5, low >> 8)
    self._device.write8(6, high & 255)
    self._device.write8(7, high >> 8)