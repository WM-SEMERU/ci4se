def p_xor_p_expression(tok):
    if len(tok) == 4:
        tok[0] = LogicalBinOpRule(tok[2], tok[1], tok[3])
    else:
        tok[0] = tok[1]