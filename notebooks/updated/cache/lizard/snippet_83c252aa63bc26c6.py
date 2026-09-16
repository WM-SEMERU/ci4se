def current_frame(self, n):
    self.sound.seek(n)
    self._current_frame = n