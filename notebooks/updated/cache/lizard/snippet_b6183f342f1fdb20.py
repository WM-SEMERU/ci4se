def get_bytes(self, n):
    b = self.packet.read(n)
    if len(b) < n:
        return b + '\x00' * (n - len(b))
    return b