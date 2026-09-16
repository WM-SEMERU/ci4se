def sign(self, keys):
    key = keys[0]
    signed = self.raw()[-2:]
    signing = base64.b64encode(key.signature(bytes(signed, 'ascii')))
    self.signatures = [signing.decode('ascii')]