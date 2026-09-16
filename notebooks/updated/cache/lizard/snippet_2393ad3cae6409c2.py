def p_rddl_block(self, p):
    if p[1] is None:
        p[0] = dict()
    else:
        name, block = p[2]
        p[1][name] = block
        p[0] = p[1]