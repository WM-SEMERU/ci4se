def regs(self):
    regs = set()
    for operand in self.operands:
        if not operand.type.has_reg:
            continue
        regs.update(operand.regs)
    return regs