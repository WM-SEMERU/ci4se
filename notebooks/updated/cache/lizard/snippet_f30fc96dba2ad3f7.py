def set_hue(self, value):
    old = self._hue
    self._hue = value
    if value != old:
        self._fill()
        self.event_generate('<<ColorChanged>>')