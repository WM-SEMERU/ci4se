def set_vibration(self, left_motor, right_motor, duration):
    if left_motor and right_motor:
        return self._spin_up(self.double_rumble, duration / 1000)
    if left_motor:
        return self._spin_up(self.left_rumble, duration / 1000)
    if right_motor:
        return self._spin_up(self.right_rumble, duration / 1000)
    return -1