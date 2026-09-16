def add_size(self, n):
    self.packet.write(struct.pack('>I', n))
    return self