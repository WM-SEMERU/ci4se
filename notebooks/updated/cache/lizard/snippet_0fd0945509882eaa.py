def p_iteration_statement_6(self, p):
    vardecl = self.asttypes.VarDeclNoIn(identifier=p[4], initializer=p[5])
    vardecl.setpos(p, 3)
    p[0] = self.asttypes.ForIn(item=vardecl, iterable=p[7], statement=p[9])
    p[0].setpos(p)