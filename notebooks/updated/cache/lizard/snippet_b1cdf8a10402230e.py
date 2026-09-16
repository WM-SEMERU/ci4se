def p_class_constant(p):
    p[0] = ast.StaticProperty(p[1], p[3], lineno=p.lineno(2))