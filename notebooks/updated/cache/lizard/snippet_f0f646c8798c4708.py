def bytes(self):
    if self.asm not in ('DEFB', 'DEFS', 'DEFW'):
        if self.pending:
            tmp = self.arg
            self.arg = tuple([0] * self.arg_num)
            result = super(Asm, self).bytes()
            self.arg = tmp
            return result
        return super(Asm, self).bytes()
    if self.asm == 'DEFB':
        if self.pending:
            return tuple([0] * self.arg_num)
        return tuple([(x & 255) for x in self.argval()])
    if self.asm == 'DEFS':
        if self.pending:
            N = self.arg[0]
            if isinstance(N, Expr):
                N = N.eval()
            return tuple([0] * N)
        args = self.argval()
        num = args[1] & 255
        return tuple([num] * args[0])
    if self.pending:
        return tuple([0] * 2 * self.arg_num)
    result = ()
    for i in self.argval():
        x = i & 65535
        result += x & 255, x >> 8
    return result