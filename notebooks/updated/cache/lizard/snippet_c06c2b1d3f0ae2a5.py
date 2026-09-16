def set_regs(self, regs_dump):
    if self.real_stack_top == 0 and self.adjust_stack is True:
        raise SimStateError(
            "You need to set the stack first, or setadjust_stack to False. Beware that in this case, sp and bp won't be updated"
            )
    data = self._read_data(regs_dump)
    rdata = re.split(b'\n', data)
    for r in rdata:
        if r == b'':
            continue
        reg = re.split(b' +', r)[0].decode()
        val = int(re.split(b' +', r)[1], 16)
        try:
            self.state.registers.store(reg, claripy.BVV(val, self.state.
                arch.bits))
        except KeyError as e:
            l.warning('Reg %s was not set', e)
    self._adjust_regs()