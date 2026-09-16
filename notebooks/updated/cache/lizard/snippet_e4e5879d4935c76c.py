def p_numeric_literal(self, p):
    p[0] = self.asttypes.Number(p[1])
    p[0].setpos(p)