def get_target(self, offset, extended_arg=0):
    inst = self.get_inst(offset)
    if inst.opcode in self.opc.JREL_OPS | self.opc.JABS_OPS:
        target = inst.argval
    else:
        target = next_offset(inst.opcode, self.opc, inst.offset)
    return target