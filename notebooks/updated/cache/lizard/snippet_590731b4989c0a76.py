def string_addresses(self, encoding=None):
    if not encoding:
        encoding = self.encoding
    return [Address(i.address).encode(encoding).decode(encoding) for i in self]