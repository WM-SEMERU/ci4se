def communicate_through(self, file):
    if self._communication is not None:
        raise ValueError('Already communicating.')
    self._communication = communication = Communication(file, self.
        _get_needle_positions, self._machine, [self._on_message_received],
        right_end_needle=self.right_end_needle, left_end_needle=self.
        left_end_needle)
    return communication