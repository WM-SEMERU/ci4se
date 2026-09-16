def p_function(self, p):
    p[0] = ast.Function(name=p[3], parameters=p[5], return_type=p[2],
        exceptions=p[7], oneway=p[1], annotations=p[8], lineno=p.lineno(3))