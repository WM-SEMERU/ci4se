def _split_index(self, key):
    if not isinstance(key, tuple):
        key = key,
    elif key == ():
        return (), ()
    if key[0] is Ellipsis:
        num_pad = self.ndims - len(key) + 1
        key = (slice(None),) * num_pad + key[1:]
    elif len(key) < self.ndims:
        num_pad = self.ndims - len(key)
        key = key + (slice(None),) * num_pad
    map_slice = key[:self.ndims]
    if self._check_key_type:
        map_slice = self._apply_key_type(map_slice)
    if len(key) == self.ndims:
        return map_slice, ()
    else:
        return map_slice, key[self.ndims:]