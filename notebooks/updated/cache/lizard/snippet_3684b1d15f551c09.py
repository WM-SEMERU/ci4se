def p_variable_declaration(self, p):
    if len(p) == 2:
        p[0] = ast.VarDecl(p[1])
    else:
        p[0] = ast.VarDecl(p[1], p[2])