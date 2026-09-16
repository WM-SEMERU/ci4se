def drive(self):
    if self.is_drive:
        return self
    cleartext = self.luks_cleartext_slave
    if cleartext:
        return cleartext.drive
    if self.is_block:
        return self._daemon[self._P.Block.Drive]
    return None