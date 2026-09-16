def _add32(ins):
    op1, op2 = tuple(ins.quad[2:])
    if _int_ops(op1, op2) is not None:
        o1, o2 = _int_ops(op1, op2)
        if int(o2) == 0:
            output = _32bit_oper(o1)
            output.append('push de')
            output.append('push hl')
            return output
    if op1[0] == '_' and op2[0] != '_':
        op1, op2 = op2, op1
    if op2[0] == '_':
        output = _32bit_oper(op1)
        output.append('ld bc, (%s)' % op2)
        output.append('add hl, bc')
        output.append('ex de, hl')
        output.append('ld bc, (%s + 2)' % op2)
        output.append('adc hl, bc')
        output.append('push hl')
        output.append('push de')
        return output
    output = _32bit_oper(op1, op2)
    output.append('pop bc')
    output.append('add hl, bc')
    output.append('ex de, hl')
    output.append('pop bc')
    output.append('adc hl, bc')
    output.append('push hl')
    output.append('push de')
    return output