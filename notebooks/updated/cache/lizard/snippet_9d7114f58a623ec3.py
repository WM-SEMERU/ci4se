def p_formula_atom(self, p):
    if p[1] == Symbols.TRUE.value:
        p[0] = PLTrue()
    elif p[1] == Symbols.FALSE.value:
        p[0] = PLFalse()
    else:
        p[0] = PLAtomic(Symbol(p[1]))