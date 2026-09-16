def serial(self, may_block=True):
    if not self.capabilities.have_serial_number():
        raise yubikey_base.YubiKeyVersionError(
            'Serial number unsupported in YubiKey %s' % self.version())
    return self._read_serial(may_block)