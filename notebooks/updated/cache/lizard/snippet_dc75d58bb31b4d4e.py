def sec_as_hex(self, is_compressed=None):
    sec = self.sec(is_compressed=is_compressed)
    return self._network.sec_text_for_blob(sec)