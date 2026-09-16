def p_field_expr(p):
    p[0] = node.expr(op='.', args=node.expr_list([p[1], node.ident(name=p[2
        ], lineno=p.lineno(2), lexpos=p.lexpos(2))]))