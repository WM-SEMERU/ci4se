def _initialize(self):
    self._header.value = b'\xaaU'
    self._current_state.value = b'\x00\x00'
    s = self._generate_packet()
    self._ser.write(s)
    self._header.value = b'\xaa\xaa'
    self._current_state.value = b'\x02\x01'
    return self._read_existing_recipe()