def instruction_ROR_register(self, opcode, register):
    a = register.value
    r = self.ROR(a)
    register.set(r)