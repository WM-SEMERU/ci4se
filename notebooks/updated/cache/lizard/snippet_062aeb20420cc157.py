def unlink_chunk(self, x, z):
    if self.size < 2 * SECTOR_LENGTH:
        return
    self.file.seek(4 * (x + 32 * z))
    self.file.write(pack('>IB', 0, 0)[1:])
    self.file.seek(SECTOR_LENGTH + 4 * (x + 32 * z))
    self.file.write(pack('>I', 0))
    current = self.metadata[x, z]
    free_sectors = self._locate_free_sectors(ignore_chunk=current)
    truncate_count = list(reversed(free_sectors)).index(False)
    if truncate_count > 0:
        self.size = SECTOR_LENGTH * (len(free_sectors) - truncate_count)
        self.file.truncate(self.size)
        free_sectors = free_sectors[:-truncate_count]
    for s in range(current.blockstart, min(current.blockstart + current.
        blocklength, len(free_sectors))):
        if free_sectors[s]:
            self.file.seek(SECTOR_LENGTH * s)
            self.file.write(SECTOR_LENGTH * b'\x00')
    self.metadata[x, z] = ChunkMetadata(x, z)