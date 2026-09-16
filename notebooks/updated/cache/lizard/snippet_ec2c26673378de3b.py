def p_expr(self, p):
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ast.Comma(left=p[1], right=p[3])