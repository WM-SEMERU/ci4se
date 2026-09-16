def move_to_limit(self, position):
    cmd = 'MOVE', [Float, Integer]
    self._write(cmd, position, 1)