def access_key(self, data):
    if data.startswith(b'h:'):
        new = binascii.unhexlify(data[2:])
    else:
        new = data
    if len(new) == 6:
        self.access_code = new
    else:
        raise yubico_exception.InputError('Access key must be exactly 6 bytes')