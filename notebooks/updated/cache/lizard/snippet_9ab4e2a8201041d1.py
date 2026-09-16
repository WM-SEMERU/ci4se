def _normalize_keys(self, data):
    encode = self.encoder.encode
    decode = self.encoder.decode
    return {decode(encode(k)): v for k, v in iteritems(data)}