def query_sequence(self):
    if not self.entries.seq:
        return None
    if self.check_flag(16):
        return rc(self.entries.seq)
    return self.entries.seq