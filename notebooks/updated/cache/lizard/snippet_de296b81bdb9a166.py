def p_try_statement_1(self, p):
    p[0] = self.asttypes.Try(statements=p[2], catch=p[3])
    p[0].setpos(p)