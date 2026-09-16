def _is(self, r, val):
    if not is_register(r) or val is None:
        return False
    r = r.lower()
    if is_register(val):
        return self.eq(r, val)
    if is_number(val):
        val = str(valnum(val))
    else:
        val = str(val)
    if val[0] == '(':
        val = self.mem[val[1:-1]]
    return self.regs[r] == val