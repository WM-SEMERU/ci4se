def _ne16(ins):
    output = _16bit_oper(ins.quad[2], ins.quad[3])
    output.append('or a')
    output.append('sbc hl, de')
    output.append('ld a, h')
    output.append('or l')
    output.append('push af')
    return output