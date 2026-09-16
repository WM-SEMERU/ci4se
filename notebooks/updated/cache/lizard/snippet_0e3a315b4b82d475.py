def names(self):
    return tuple(sorted({instr.arg for instr in self.instrs if instr.
        uses_name}))