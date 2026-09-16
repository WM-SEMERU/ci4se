def add_inote(self, msg, idx, off=None):
    if off is not None:
        idx = self.off_to_pos(off)
    if idx not in self.notes:
        self.notes[idx] = []
    self.notes[idx].append(msg)