def _bnot16(ins):
    output = _16bit_oper(ins.quad[2])
    output.append('call __BNOT16')
    output.append('push hl')
    REQUIRES.add('bnot16.asm')
    return output