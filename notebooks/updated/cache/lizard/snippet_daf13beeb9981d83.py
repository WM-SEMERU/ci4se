def memory_read16(self, addr, num_halfwords, zone=None):
    return self.memory_read(addr, num_halfwords, zone=zone, nbits=16)