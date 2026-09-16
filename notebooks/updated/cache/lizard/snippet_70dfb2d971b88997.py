def sec(self, is_compressed=None):
    if is_compressed is None:
        is_compressed = self.is_compressed()
    public_pair = self.public_pair()
    if public_pair is None:
        return None
    return public_pair_to_sec(public_pair, compressed=is_compressed)