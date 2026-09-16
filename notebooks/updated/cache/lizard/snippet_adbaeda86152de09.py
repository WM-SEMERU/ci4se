def _load32(ins):
    output = _32bit_oper(ins.quad[2])
    output.append('push de')
    output.append('push hl')
    return output