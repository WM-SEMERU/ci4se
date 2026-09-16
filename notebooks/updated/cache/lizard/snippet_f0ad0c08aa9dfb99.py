def p_pvar_list(self, p):
    if p[1] is None:
        p[0] = []
    else:
        p[1].append(p[2])
        p[0] = p[1]