def instruction_ROL_register(self, opcode, register):
    a = register.value
    r = self.ROL(a)
    register.set(r)