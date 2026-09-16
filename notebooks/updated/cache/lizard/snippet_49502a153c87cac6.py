def p_new_else_single(p):
    if len(p) == 4:
        p[0] = ast.Else(ast.Block(p[3], lineno=p.lineno(2)), lineno=p.lineno(1)
            )