def get_chunk(self, x, z):
    return self.chunkclass(self.get_nbt(x, z))