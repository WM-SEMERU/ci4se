def move_backward(self, seconds=None):
    self._move(speed=-SPEED_MAX, steering=0, seconds=seconds)