def write_event(self, etype, code, value):
    last_value = self._write_cache.get(code)
    if last_value != value:
        self.device.write(etype, code, value)
        self._write_cache[code] = value