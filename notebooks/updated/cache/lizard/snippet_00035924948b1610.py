def p_labelled_statement(self, p):
    p[0] = self.asttypes.Label(identifier=p[1], statement=p[3])
    p[0].setpos(p, 2)