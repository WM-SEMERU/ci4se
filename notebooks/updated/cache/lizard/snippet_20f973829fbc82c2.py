def unlock(self, password: str):
    if self.locked:
        self._privkey = decode_keyfile_json(self.keystore, password.encode(
            'UTF-8'))
        self.locked = False
        self._fill_address()