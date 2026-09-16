def generate(self, v):
    val = v.tostring(self.encoding)
    return '({lhs} {op} {val})'.format(lhs=self.lhs, op=self.op, val=val)