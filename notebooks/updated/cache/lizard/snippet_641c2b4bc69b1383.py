def p_pvar_expr(self, p):
    if len(p) == 2:
        p[0] = 'pvar_expr', (p[1], None)
    elif len(p) == 5:
        p[0] = 'pvar_expr', (p[1], p[3])