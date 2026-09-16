def buttons_pressed(self):
    for b in self._buffer_cache:
        fcntl.ioctl(self._button_file(b), self.EVIOCGKEY, self._buffer_cache[b]
            )
    pressed = []
    for k, v in self._buttons.items():
        buf = self._buffer_cache[v['name']]
        bit = v['value']
        if bool(buf[int(bit / 8)] & 1 << bit % 8):
            pressed.append(k)
    return pressed