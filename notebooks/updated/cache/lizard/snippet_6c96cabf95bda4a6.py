def _jog(self, axis, direction, step):
    jog(axis, direction, step, self.hardware, self._current_mount)
    self.current_position = self._position()
    return 'Jog: {}'.format([axis, str(direction), str(step)])