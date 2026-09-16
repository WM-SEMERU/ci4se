def _write(self, frame):
    for data in frame.to_feature_reports(debug=self.debug):
        debug_str = None
        if self.debug:
            data, debug_str = data
        self._waitfor_clear(yubikey_defs.SLOT_WRITE_FLAG)
        self._raw_write(data, debug_str)
    return True