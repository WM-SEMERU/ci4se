def p_global_stmt(p):
    p[0] = node.global_stmt(p[2])
    for ident in p[0]:
        ident.props = 'G'