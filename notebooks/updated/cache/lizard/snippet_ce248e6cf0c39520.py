def delete(self, key):
    validate_is_bytes(key)
    self.root_hash = self._set(self.root_hash, encode_to_bin(key), b'')