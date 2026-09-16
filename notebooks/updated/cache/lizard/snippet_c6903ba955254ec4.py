def hexdigest(self, data=None):
    from base64 import b16encode
    if pyver == 2:
        return b16encode(self.digest(data))
    else:
        return b16encode(self.digest(data)).decode('us-ascii')