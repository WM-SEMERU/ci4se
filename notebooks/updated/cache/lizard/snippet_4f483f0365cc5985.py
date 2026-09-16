def _jzerof(ins):
    value = ins.quad[1]
    if is_float(value):
        if float(value) == 0:
            return ['jp %s' % str(ins.quad[2])]
        else:
            return []
    output = _float_oper(value)
    output.append('ld a, c')
    output.append('or l')
    output.append('or h')
    output.append('or e')
    output.append('or d')
    output.append('jp z, %s' % str(ins.quad[2]))
    return output