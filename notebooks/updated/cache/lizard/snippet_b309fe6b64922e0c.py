def i2m(self, pkt, x):
    if x is None:
        x = 0
    elif isinstance(x, str):
        return bytes_encode(x)
    return x