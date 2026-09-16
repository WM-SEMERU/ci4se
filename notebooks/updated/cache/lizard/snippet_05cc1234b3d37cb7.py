def _and8(ins):
    op1, op2 = tuple(ins.quad[2:])
    if _int_ops(op1, op2) is not None:
        op1, op2 = _int_ops(op1, op2)
        output = _8bit_oper(op1)
        if op2 != 0:
            output.append('push af')
            return output
        output.append('xor a')
        output.append('push af')
        return output
    output = _8bit_oper(op1, op2)
    lbl = tmp_label()
    output.append('or a')
    output.append('jr z, %s' % lbl)
    output.append('ld a, h')
    output.append('%s:' % lbl)
    output.append('push af')
    return output