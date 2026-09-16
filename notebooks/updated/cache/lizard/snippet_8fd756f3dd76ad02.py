def instruction_BVS(self, opcode, ea):
    if self.V == 1:
        self.program_counter.set(ea)