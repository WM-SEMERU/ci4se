def position_i(self):
    self._position_i, value = self.get_attr_int(self._position_i, 'hold_pid/Ki'
        )
    return value