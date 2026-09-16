def instruction_BSR_JSR(self, opcode, ea):
    self.push_word(self.system_stack_pointer, self.program_counter.value)
    self.program_counter.set(ea)