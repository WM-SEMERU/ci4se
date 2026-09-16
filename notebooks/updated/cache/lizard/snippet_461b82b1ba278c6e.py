def add(self, key, value, time, compress_level=-1):
    return self._set_add_replace('add', key, value, time, compress_level=
        compress_level)