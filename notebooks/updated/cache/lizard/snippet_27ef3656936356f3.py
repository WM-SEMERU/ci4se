def last_part_number(self):
    return int(self.size / self.chunk_size
        ) if self.size % self.chunk_size else int(self.size / self.chunk_size
        ) - 1