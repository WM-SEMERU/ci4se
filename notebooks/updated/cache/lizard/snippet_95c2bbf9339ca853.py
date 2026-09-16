def p_function_declaration(self, p):
    if len(p) == 8:
        p[0] = self.asttypes.FuncDecl(identifier=p[2], parameters=None,
            elements=p[6])
    else:
        p[0] = self.asttypes.FuncDecl(identifier=p[2], parameters=p[4],
            elements=p[7])
    p[0].setpos(p)