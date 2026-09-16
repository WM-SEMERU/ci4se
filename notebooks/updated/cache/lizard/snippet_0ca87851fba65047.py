def begin(self):
    self._device.writeList(HT16K33_SYSTEM_SETUP | HT16K33_OSCILLATOR, [])
    self.set_blink(HT16K33_BLINK_OFF)
    self.set_brightness(15)