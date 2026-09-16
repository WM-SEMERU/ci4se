def p_matrix(p):
    if len(p) == 3:
        p[0] = node.matrix()
    else:
        p[0] = node.matrix(p[2])