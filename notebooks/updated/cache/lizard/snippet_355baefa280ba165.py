def _addf(ins):
    op1, op2 = tuple(ins.quad[2:])
    if _f_ops(op1, op2) is not None:
        opa, opb = _f_ops(op1, op2)
        if opb == 0:
            output = _float_oper(opa)
            output.extend(_fpush())
            return output
    output = _float_oper(op1, op2)
    output.append('call __ADDF')
    output.extend(_fpush())
    REQUIRES.add('addf.asm')
    return output