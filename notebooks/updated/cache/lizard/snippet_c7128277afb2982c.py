def get_instruction(self, idx, off=None):
    if off != None:
        idx = self.off_to_pos(off)
    return [i for i in self.get_instructions()][idx]